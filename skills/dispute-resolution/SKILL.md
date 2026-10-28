---
name: dispute-resolution
description: Analyser le droit applicable, la juridiction compétente, l'arbitrage et la médiation ou conciliation préalable. À charger pour toute clause sur les litiges ou la loi du contrat.
---

# Droit applicable et règlement des litiges

## Points de contrôle
1. **Droit applicable** : est-il indiqué ? S'il est absent, signale-le dans `alertes_contexte` et applique la présomption du mandat (droit français) en le précisant.
2. **Juridiction** : tribunal désigné. Un for éloigné de la partie représentée (autre pays, autre continent) renchérit fortement tout litige : frais d'avocats locaux, traduction, déplacements. Si seul le for est indiqué, l'absence de droit applicable explicite crée une incertitude supplémentaire.
3. **Cohérence** : droit d'un pays + tribunaux d'un autre pays = coûteux et incertain → `incoherences` si contradictoire.
4. **Arbitrage** : institution, siège, langue, nombre d'arbitres. Coût élevé pour les petits litiges.
5. **Préalable amiable** : médiation ou conciliation obligatoire avant tout procès, avec un délai.
6. **Langue** : version qui fait foi en cas de traduction.

## Grille
- ELEVE : juridiction exclusive à l'étranger alors que les deux parties sont établies en France ; arbitrage international pour un contrat de faible montant.
- MOYEN : droit applicable absent ; pas de préalable amiable.
- FAIBLE : juridiction française mais éloignée du siège de la partie représentée.

## Reformulation type
« Le contrat est régi par le droit français. Les parties chercheront une solution amiable pendant trente (30) jours. À défaut, tout litige sera soumis aux tribunaux compétents de [ville du siège de la partie représentée]. »
