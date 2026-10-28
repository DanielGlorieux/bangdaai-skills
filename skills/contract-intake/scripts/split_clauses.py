"""Découpe un contrat texte en clauses : python3 split_clauses.py contrat.txt -> JSON sur stdout."""
import json
import re
import sys

# "Article 4", "Art. 4.2", "ARTICLE 12 -" ou "4." / "4.2" en début de ligne
HEADER = re.compile(
    r"^\s*(?:(?:article|art\.?)\s*(\d+(?:\.\d+)*)|(\d+(?:\.\d+)*)[.)])\s*[-–:.]?\s*(.*)$",
    re.IGNORECASE,
)


def split(text):
    clauses, current = [], None
    preamble = []
    for line in text.splitlines():
        m = HEADER.match(line)
        if m:
            if current:
                clauses.append(current)
            num = m.group(1) or m.group(2)
            current = {"ref": f"Art. {num}", "titre": m.group(3).strip(), "texte": line.strip()}
        elif current:
            if line.strip():
                current["texte"] += "\n" + line.strip()
        elif line.strip():
            preamble.append(line.strip())
    if current:
        clauses.append(current)
    if preamble:
        clauses.insert(0, {"ref": "Préambule", "titre": "", "texte": "\n".join(preamble)})
    return clauses


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        print(json.dumps(split(f.read()), ensure_ascii=False, indent=1))
