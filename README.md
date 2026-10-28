# BangdaAI — skills d'analyse de contrats

Skills de l'agent **BangdaAI** (harnais [TrueForge](https://www.npmjs.com/package/@truefoundry/trueforge)), un analyste juridique de premier niveau qui relit un contrat clause par clause et signale les clauses à risque pour la partie représentée.

Projet réalisé dans le cadre du Master 2 Intelligence Artificielle — ILBOUDO P. Daniel Glorieux.

> ⚠️ Analyse automatisée destinée à être validée par un professionnel du droit. Ces skills ne constituent pas un avis juridique.

## Les 13 skills

| Étape | Skill | Rôle |
|---|---|---|
| 1. Identification | `contract-intake` | Type, parties, objet, durée, droit applicable ; découpage en clauses (`scripts/split_clauses.py`) |
| 2. Playbook | `risk-playbook-saas` | Points de contrôle d'un contrat SaaS / abonnement logiciel |
| | `risk-playbook-prestation` | Prestation de services (playbook par défaut) |
| | `risk-playbook-nda` | Accord de confidentialité |
| | `risk-playbook-bail` | Bail |
| 3. Analyse thématique | `liability-indemnity` | Responsabilité, plafonds, garanties, pénalités |
| | `termination-renewal` | Durée, reconduction, résiliation, réversibilité |
| | `data-privacy` | Données personnelles (RGPD), sécurité, sous-traitants |
| | `ip-confidentiality` | Propriété intellectuelle, confidentialité, non-concurrence |
| | `dispute-resolution` | Droit applicable, juridiction, arbitrage, médiation |
| 4. Finalisation | `missing-clauses` | Clauses absentes attendues pour le type de contrat |
| | `redline-drafting` | Reformulations négociables |
| | `citation-verifier` | Vérification des citations avant réponse (`scripts/verify_citations.py`) |

## Utilisation dans TrueForge

Déclarer chaque skill comme source Git :

```json
{ "manifest": { "type": "git", "name": "contract-intake",
  "url": "https://github.com/DanielGlorieux/bangdaai-skills",
  "path": "skills/contract-intake", "ref": "main",
  "description": "..." } }
```

Les skills sont téléchargés dans la sandbox de l'agent : la sandbox doit être activée.
