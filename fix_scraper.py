from pathlib import Path

path = Path(r'd:\Docusign exam\scrape_docusign_study_material.py')
text = path.read_text(encoding='utf-8')
old = '''        if node.name == "pre":
            content = node.get_text()
            return f"```\n{content.rstrip()}\n```\n\n"'''
new = '''        if node.name == "pre":
            content = node.get_text()
            return "```\n" + content.rstrip() + "\n```\n\n"'''

if old not in text:
    print('old text not found')
    import sys
    sys.exit(1)

path.write_text(text.replace(old, new), encoding='utf-8')
print('patched')
