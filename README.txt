LE BOUCHONNEUR — VERSION 5.1

Mise à jour
1. Télécharge et décompresse cette archive.
2. Dans ton dépôt GitHub Pages habituel, remplace les fichiers de l'ancienne version par ceux du dossier le-bouchonneur-v4.
3. Conserve le dossier assets et ses images.
4. Recharge l'application. Les données existantes du navigateur sont conservées ; exporte néanmoins une sauvegarde JSON avant la mise à jour.

Accueil
- Deux indicateurs uniquement : valorisation du portefeuille et dividendes annuels bruts estimés.
- Deux camemberts empilés verticalement : allocation du portefeuille puis dividendes nets estimés par action.

Portefeuille
- Suppression du bouton et de l'encart d'import CSV des dividendes.
- Actualisation des cours et bouton d'actualisation des dividendes Boursorama.
- Les actions qui correspondent aux lignes du palmarès Boursorama reçoivent automatiquement une prévision annuelle par action.
- La version retient par défaut la colonne Div. 2027, car il s'agit de l'année future de référence au moment de la création de cette version.
- Si une action ne figure pas dans le palmarès, tu peux ajouter son dividende manuellement dans Modifier.
- Les modifications manuelles restent prioritaires lors des actualisations.
- Après le versement, supprimer la modification manuelle restaure la prévision Boursorama d'origine lorsqu'elle existe.

Source et limites importantes
- Source affichée : https://www.boursorama.com/bourse/actions/palmares/dividendes/
- Boursorama affiche des estimations annuelles par action (Div. 2026 / Div. 2027). Ces montants ne constituent pas une annonce officielle et ne donnent pas forcément les dates de détachement et de paiement.
- La récupération parcourt plusieurs pages du palmarès (jusqu’à la page 5) via le relais public AllOrigins (api.allorigins.win), car l'application est hébergée sur GitHub Pages et ne peut pas nécessairement lire directement le site Boursorama à cause des règles CORS.
- Ce relais gratuit est un service tiers : il peut être indisponible, limité ou bloqué. Si l'actualisation échoue, les données déjà enregistrées restent présentes et la saisie manuelle reste possible.
- Le palmarès est une sélection, pas l'ensemble des sociétés cotées. Une société absente est laissée à la saisie manuelle.
- Le rapprochement se fait par nom de société et une liste d'alias pour les principales valeurs françaises. Vérifie le ticker et le montant affichés lors des premiers tests.

Fiscalité et sauvegardes
- Le taux CTO reste modifiable. Le net est une estimation calculée à partir du taux choisi.
- Les données sont stockées localement dans le navigateur. Exporte régulièrement une sauvegarde JSON, en particulier avant de changer d'appareil.

Correctif V5.1 : recherche étendue à plusieurs pages du palmarès afin de retrouver les valeurs comme TotalEnergies (TTE), qui ne figurent pas nécessairement sur la première page. Le nombre de pages réellement lues est affiché dans le statut d’actualisation.
