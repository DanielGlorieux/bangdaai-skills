---
name: missing-clauses
description: Lister les clauses absentes qui devraient figurer dans ce type de contrat. À charger après l'analyse clause par clause, pour remplir clauses_manquantes.
---

# Clauses manquantes

Coche chaque ligne pour le type de contrat identifié. Une clause n'est « manquante » que si tu as vérifié qu'aucun article ne la traite, même sous un autre titre.

| Clause | SaaS | Prestation | NDA | Bail | Niveau si absente |
|---|---|---|---|---|---|
| Niveau de service (SLA) / disponibilité | ✔ | | | | MOYEN (ELEVE si service critique) |
| Réversibilité / restitution des données | ✔ | ✔ | | | ELEVE |
| Sécurité et notification des violations | ✔ | ✔ | | | ELEVE |
| Accord de sous-traitance RGPD (DPA) | ✔ | ✔ si données perso | | | ELEVE |
| Plan de continuité / sauvegardes | ✔ | | | | MOYEN |
| Recette des livrables | | ✔ | | | MOYEN |
| Propriété intellectuelle | ✔ | ✔ | ✔ | | ELEVE si livrables |
| Confidentialité | ✔ | ✔ | — | | MOYEN |
| Plafond de responsabilité | ✔ | ✔ | | | MOYEN |
| Assurance | | ✔ | | ✔ | FAIBLE |
| Force majeure | ✔ | ✔ | | ✔ | FAIBLE |
| Résiliation pour manquement | ✔ | ✔ | | ✔ | MOYEN |
| Exclusions de confidentialité | | | ✔ | | MOYEN |
| Restitution des informations | | | ✔ | | MOYEN |
| État des lieux / dépôt de garantie | | | | ✔ | MOYEN |
| Droit applicable | ✔ | ✔ | ✔ | ✔ | FAIBLE (MOYEN si for étranger) |
| Juridiction / règlement amiable | ✔ | ✔ | ✔ | ✔ | FAIBLE |

Format de sortie pour chaque clause manquante :
`{"clause": "...", "pourquoi": "conséquence concrète de l'absence pour la partie représentée", "niveau": "..."}`
