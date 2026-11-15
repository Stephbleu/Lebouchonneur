LE BOUCHONNEUR V6.1

MISE A JOUR AUTOMATIQUE DES COURS ET DIVIDENDES
- Une tâche GitHub Actions (.github/workflows/update-quotes.yml) s'exécute chaque soir de bourse
  et lance scripts/update_quotes.py, qui interroge Yahoo Finance puis écrit data/quotes.csv.
- Le bouton "Actualiser le cours" lit data/quotes.csv (même site : aucun blocage CORS).
  Au lancement, l'application le fait aussi automatiquement si les données ont plus de 6 h.
- Les titres à suivre sont listés dans data/tickers.csv (colonnes : ticker, name, yahoo).
  Colonne "yahoo" = symbole Yahoo Finance (ex. TTE.PA). Ajoute une ligne pour suivre un nouveau titre.

IMPORT MANUEL (secours)
CSV attendu : ticker,name,price,dividend2026,forecast2027
Les dividendes sont en euros bruts par action. Les cellules vides ne remplacent pas les valeurs existantes.
Exporter une sauvegarde JSON avant remplacement.

METHODE DE PREVISION (forecast2027)
  base       = dividendes détachés sur les 12 derniers mois
  croissance = croissance annuelle moyenne des 3 dernières années complètes, bornée à +/-20 %
  prévision  = base x (1 + croissance)
C'est une extrapolation de l'historique, pas une prévision d'analystes.

CHANGEMENT D'ANNEE
Les colonnes du CSV s'appellent dividend2026 et forecast2027 (noms attendus par l'application).
En 2027 : "dividend2026" contiendra les dividendes de 2027 et "forecast2027" la prévision 2028,
tant que les libellés de l'application n'ont pas été mis à jour.
