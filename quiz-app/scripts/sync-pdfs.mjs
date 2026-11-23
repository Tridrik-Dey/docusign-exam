// Copy the study PDFs from ../output/pdf into public/pdf so the study plan can open them.
import { cpSync, existsSync, mkdirSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, '..', '..', 'output', 'pdf');
const dest = join(here, '..', 'public', 'pdf');
if (!existsSync(src)) {
  console.warn(`sync-pdfs: ${src} not found, skipping`);
} else {
  mkdirSync(dest, { recursive: true });
  cpSync(src, dest, { recursive: true, filter: (p) => !p.endsWith('.png') });
  const count = readdirSync(dest).length + (existsSync(join(dest, 'sections')) ? readdirSync(join(dest, 'sections')).length : 0);
  console.log(`sync-pdfs: copied study PDFs to public/pdf (${count} entries)`);
}
