from pathlib import Path

import pdfplumber


ROOT = Path(".")
TMP = ROOT / "tmp" / "pdfs"
TMP.mkdir(parents=True, exist_ok=True)

PDFS = {
    "combined_qa": Path(r"C:\Users\Admin\Downloads\Docusign_Combined_QA_Explained.pdf"),
    "prep_guide": Path(r"C:\Users\Admin\Downloads\Certified_Docusign_IAM_Integration_&_Extension_Developer_Prep_Guide_(v._2026).pdf"),
}


def extract_pdf(path: Path) -> str:
    parts = []
    with pdfplumber.open(path) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            parts.append(f"\n\n--- PAGE {index} ---\n\n{text.strip()}")
    return "\n".join(parts).strip() + "\n"


def main() -> None:
    for name, path in PDFS.items():
        text = extract_pdf(path)
        output = TMP / f"{name}.txt"
        output.write_text(text, encoding="utf-8")
        print(f"{name}: {len(text)} chars -> {output}")


if __name__ == "__main__":
    main()
