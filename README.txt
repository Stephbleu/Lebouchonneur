LE BOUCHONNEUR — VERSION 4.0

Installation / mise à jour
1. Décompresse l'archive.
2. Dans le dépôt GitHub Pages existant, remplace les anciens fichiers par ceux du dossier portefeuille-boursier-v3.
3. Conserve bien le dossier assets avec ses images.
4. Attends quelques instants puis recharge le site. Si l'ancienne version reste affichée, ferme puis rouvre Chrome ou vide le cache du site.

Nouveautés V4
- Deux graphiques en camembert sur l'accueil : répartition du portefeuille et dividendes nets estimés par action.
- Plus de page séparée « Dividendes ».
- Bouton « Modifier » sur chaque ligne du portefeuille : modification de la quantité et du cours.
- Dans ce même panneau, gestion des dividendes de l'action : montant brut par action, date de détachement, date de paiement et statut.
- Import des dividendes par fichier CSV depuis le portefeuille.
- Les modifications manuelles restent prioritaires et ne sont pas écrasées par les imports.
- Après versement, le bouton « Supprimer la modification manuelle » permet de revenir à la donnée importée. Si la ligne était uniquement manuelle, elle est supprimée.
- Les cours continuent à être importés depuis le CSV Google Sheets configuré dans les réglages, à l'ouverture et toutes les 15 minutes.
- Sauvegarde et restauration JSON conservées.

Format du CSV dividendes
En-têtes obligatoires : ticker, amount, exDate
En-têtes facultatifs : name, payDate, status
Exemple :
ticker,name,amount,exDate,payDate,status
AI,Air Liquide,3.30,2027-05-18,2027-05-20,Prévision
TTE,TotalEnergies,3.22,2027-06-30,2027-07-02,Confirmé

Les dates doivent être au format AAAA-MM-JJ. Le montant est le dividende brut par action en euros.
L'application ne récupère pas automatiquement les dividendes depuis les sites des sociétés : l'import se fait à partir d'un fichier CSV que tu fournis. Les prévisions doivent être vérifiées auprès des sociétés avant toute décision.

Données
Les positions et dividendes sont stockés dans le navigateur (localStorage). Exporte régulièrement une sauvegarde JSON, notamment avant une mise à jour ou un changement d'appareil.
