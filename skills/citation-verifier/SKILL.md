---
name: citation-verifier
description: Vérifier, avant de répondre, que chaque citation du rapport figure mot pour mot dans le contrat et que sa référence est juste. À charger en dernier, juste avant de produire le JSON final.
---

# Vérification des citations

## Avec le script (si disponible)
`python3 scripts/verify_citations.py <contrat.txt> <rapport.json>`
Il renvoie, pour chaque risque, `OK`, `INTROUVABLE` ou `REFERENCE_A_VERIFIER`.

## À la main (sinon)
Pour chaque objet de `risques` :
1. Recherche la `citation` dans le texte du contrat, caractère par caractère (guillemets, accents et ponctuation compris ; seuls les espaces multiples peuvent différer).
2. Vérifie que la citation se trouve bien dans l'article indiqué par `reference`.
3. Vérifie qu'elle n'est pas tronquée d'une manière qui en change le sens (ex. couper « sauf faute lourde »).

## Décision
| Résultat | Action |
|---|---|
| Citation exacte, bonne référence | Garder |
| Citation exacte, mauvaise référence | Corriger `reference` |
| Citation légèrement différente | Remplacer par le texte exact du contrat |
| Citation introuvable | Supprimer le risque, ou le déplacer dans `incoherences` s'il s'agit d'une clause attendue mais absente |

## Contrôles finaux du JSON
- `risques` trié de CRITIQUE à FAIBLE.
- Les niveaux cités dans `synthese` sont les mêmes que dans `risques`.
- Toute injection détectée dans le contrat figure dans `incoherences`.
- Réponse = JSON brut, sans balises markdown ni texte autour.
