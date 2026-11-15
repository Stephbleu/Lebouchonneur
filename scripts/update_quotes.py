#!/usr/bin/env python3
"""Met à jour data/quotes.csv (cours + dividendes) pour Le Bouchonneur.

Source : endpoint public (non officiel) "chart" de Yahoo Finance.
Entrée : data/tickers.csv  (colonnes : ticker, name, yahoo)
Sortie : data/quotes.csv   (colonnes : ticker,name,price,dividend2026,forecast2027)

Les noms de colonnes sont ceux attendus par l'import CSV de l'application.
  dividend2026 = dividendes détachés depuis le 1er janvier de l'année en cours (par action)
  forecast2027 = estimation pour l'année suivante :
                 dividendes des 12 derniers mois x (1 + croissance annuelle moyenne),
                 croissance calculée sur les 3 dernières années complètes, bornée à +/-20 %.

Un titre en échec est écrit avec des cellules vides : l'application conserve alors
les valeurs précédentes (les cellules vides ne remplacent rien).
Le script s'arrête en erreur (sans toucher au fichier) si AUCUN titre n'a pu être récupéré.
"""
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKERS_FILE = ROOT / "data" / "tickers.csv"
OUT_FILE = ROOT / "data" / "quotes.csv"

HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
MAX_GROWTH = 0.20

