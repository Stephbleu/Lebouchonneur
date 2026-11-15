LE BOUCHONNEUR — VERSION 5.3

Installation
1. Exporte une sauvegarde JSON depuis Réglages > Sauvegarde.
2. Décompresse cette archive.
3. Remplace les fichiers du site GitHub Pages par le contenu du dossier le-bouchonneur-v5-2 (y compris assets/).
4. Recharge le site. Si l'ancienne version reste affichée, ferme puis rouvre l'onglet ou vide le cache du site.

Correction V5.3 — Boursorama
- L'extraction du tableau accepte maintenant les cellules d'en-tête th ou td.
- La position de la cellule contenant le nom de la société n'est plus supposée être la première colonne.
- La recherche de société utilise le texte complet de chaque ligne et les alias des tickers, notamment AI (Air Liquide), TTE (TotalEnergies) et SAF (Safran).
- La colonne du dividende 2027 est prioritaire ; la colonne 2026 sert de repli si 2027 n'est pas présente.
- Les corrections manuelles continuent de primer sur les prévisions importées.

Fonctions conservées
- Portefeuille, valorisation et graphiques.
- Actualisation des cours via Google Sheets CSV.
- Prévisions de dividendes Boursorama via relais publics, saisies et corrections manuelles.
- Sauvegarde et restauration JSON.

À savoir
Les relais publics et le HTML de Boursorama peuvent évoluer ou être indisponibles. La récupération automatique n'est donc pas garantie. Les prévisions Boursorama sont des estimations annuelles, pas des dividendes officiellement confirmés. Les données du portefeuille restent stockées dans le navigateur ; exporte régulièrement une sauvegarde JSON.
