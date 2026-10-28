---
name: risk-playbook-saas
description: Points de contrôle d'un contrat SaaS, d'abonnement logiciel, de plateforme ou d'hébergement. À charger après contract-intake quand le type est SaaS.
---

# Playbook SaaS

Vérifie chaque point, du point de vue de la partie représentée. « Client » = celui qui s'abonne.

| Thème | Standard de marché (côté Client) | Signal d'alerte |
|---|---|---|
| Disponibilité | SLA chiffré (ex. 99,5 %), pénalités ou avoirs en cas de manquement | Aucun SLA, « au mieux », disponibilité non garantie |
| Prix | Prix ferme sur la période, révision encadrée (indice, préavis, plafond) | Modification unilatérale « à tout moment » |
| Durée | Durée initiale raisonnable, préavis de non-reconduction court | Reconduction tacite longue + préavis long |
| Responsabilité | Plafond ≥ 12 mois de redevances, exclusions pour faute lourde/dolosive | Plafond symbolique (1 mois), exclusion de la perte de données |
| Données | Client propriétaire de ses données, usage limité à l'exécution du service, DPA (RGPD art. 28) | Réutilisation commerciale des données, absence de DPA |
| Réversibilité | Export des données dans un format standard, assistance en fin de contrat | Aucune clause de réversibilité ou de restitution |
| Sécurité | Mesures décrites, notification des incidents, sauvegardes | Silence total |
| Résiliation | Symétrique, pour manquement avec mise en demeure | Résiliation libre du Prestataire, indemnité totale due par le Client |
| Sous-traitance / hébergement | Liste des sous-traitants, localisation des données | Transfert hors UE non encadré |

Pour chaque thème : charge le skill thématique correspondant (`liability-indemnity`, `termination-renewal`, `data-privacy`, `ip-confidentiality`, `dispute-resolution`).
Clauses typiquement attendues pour `missing-clauses` : SLA, réversibilité, sécurité, DPA, plan de continuité, droit applicable.
