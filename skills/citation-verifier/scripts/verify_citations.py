"""Vérifie les citations d'un rapport BangdaAI : python3 verify_citations.py contrat.txt rapport.json"""
import json
import re
import sys


def normalize(s):
    s = s.replace("’", "'").replace(" ", " ").strip().strip('"«»').strip()
    return re.sub(r"\s+", " ", s)


def article_number(ref):
    m = re.search(r"\d+(?:\.\d+)*", ref or "")
    return m.group(0) if m else None


def main(contract_path, report_path):
    contract = normalize(open(contract_path, encoding="utf-8").read())
    report = json.load(open(report_path, encoding="utf-8"))
    for r in report.get("risques", []):
        quote = normalize(r.get("citation", ""))
        pos = contract.find(quote) if quote else -1
        if pos < 0:
            status = "INTROUVABLE"
        else:
            # le dernier en-tête d'article avant la citation doit correspondre à la référence
            headers = re.findall(r"(?:article|art\.?)\s*(\d+(?:\.\d+)*)", contract[:pos], re.IGNORECASE)
            expected = article_number(r.get("reference"))
            status = "OK" if not expected or (headers and headers[-1] == expected) else "REFERENCE_A_VERIFIER"
        print(f"{r.get('id', '?')}\t{status}\t{r.get('reference', '')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
