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


def reference_matches(before, expected):
    """La citation commence après `before` : vérifie qu'elle est bien dans l'article `expected`.

    Gère les articles (« Article 5 ») et les sous-articles numérotés « 5.1. » en début d'alinéa.
    """
    articles = list(re.finditer(r"(?:article|art\.?)\s*(\d+(?:\.\d+)*)", before, re.IGNORECASE))
    if not articles:
        return False
    article = articles[-1]
    # sous-articles « 5.1. » situés après le dernier en-tête d'article
    subs = re.findall(r"(?:^|\s)(\d+(?:\.\d+)+)\.\s", before[article.end():])
    current = subs[-1] if subs else article.group(1)
    if "." in expected:
        return current == expected
    # référence au niveau article (« Art. 5 ») : toute citation de l'article 5 ou de ses sous-articles convient
    return current.split(".")[0] == expected


def main(contract_path, report_path):
    contract = normalize(open(contract_path, encoding="utf-8").read())
    report = json.load(open(report_path, encoding="utf-8"))
    for r in report.get("risques", []):
        quote = normalize(r.get("citation", ""))
        pos = contract.find(quote) if quote else -1
        if pos < 0:
            status = "INTROUVABLE"
        else:
            expected = article_number(r.get("reference"))
            status = "OK" if not expected or reference_matches(contract[:pos], expected) else "REFERENCE_A_VERIFIER"
        print(f"{r.get('id', '?')}\t{status}\t{r.get('reference', '')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
