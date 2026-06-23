const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function main() {
  const outDir = process.env.TEMP || process.env.TMP || '.';

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'quiz-desktop-initial.png'), fullPage: true });

  await page.getByRole('button', { name: /^A / }).click();
  await page.getByRole('button', { name: 'Check answer' }).click();
  await page.getByText('Answer Review').waitFor();
  await page.getByText(/Why each option fits or does not fit/).waitFor();
  await page.screenshot({ path: path.join(outDir, 'quiz-desktop-reviewed.png'), fullPage: true });

  await page.getByRole('button', { name: /Next/ }).click();
  await page.getByPlaceholder('topic, section, keyword').fill('Connect');
  await page.getByText(/Question/).waitFor();
  await page.screenshot({ path: path.join(outDir, 'quiz-desktop-filtered.png'), fullPage: true });

  await page.setViewportSize({ width: 390, height: 900 });
  await page.goto('http://127.0.0.1:5173/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'quiz-mobile.png'), fullPage: true });

  const questionCount = await page.evaluate(() => {
    return fetch('/src/questions.json').then((response) => response.json()).then((items) => items.length);
  });
  if (questionCount !== 347) {
    throw new Error(`Expected 347 questions, got ${questionCount}`);
  }

  await browser.close();
  console.log(`Verified quiz app with ${questionCount} questions. Screenshots written to temp.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
