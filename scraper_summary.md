# DocuSign Study Material Scraper

This workspace contains a Python scraper to fetch the target DocuSign partner study page and convert it into Markdown.

## Files

- `scrape_docusign_study_material.py` - main scraper script.
- `requirements.txt` - Python dependencies for the scraper.
- `fix_scraper.py` - temporary fixer script used during development.

## What it does

The scraper:

- loads browser cookies from a local browser session (`chrome`, `chromium`, `edge`, or `firefox`)
- requests the starting page URL using the authenticated session
- extracts same-site links from that page
- converts HTML content into Markdown
- writes all collected content into a single `.md` output file

## Usage

1. Install dependencies:

```powershell
pip install -r "d:\Docusign exam\requirements.txt"
```

2. Log in to the site in your browser (Edge is recommended if your session is there).

3. Run the scraper:

```powershell
python "d:\Docusign exam\scrape_docusign_study_material.py" "https://dsupartners.docusign.com/page/certified-docusign-iam-integration-extension-developer" "d:\Docusign exam\study_material.md" --browser edge
```

## Notes

- The scraper uses the browser cookie store to access pages behind authenticated sessions.
- If the page is protected by a login, you must already be logged in to the selected browser.
- If the target page redirects to login, the scraper will need a valid session cookie from the browser.

## Output

- `study_material.md` will contain the scraped content once the script is run successfully.
