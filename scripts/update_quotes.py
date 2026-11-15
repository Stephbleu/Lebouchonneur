#!/usr/bin/env python3
"""Met à jour data/quotes.csv (cours + dividendes) pour Le Bouchonneur.
Entrée : data/tickers.csv (ticker, name, yahoo). Sortie : data/quotes.csv.
"""
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKERS_FILE = ROOT / "data" / "tickers.csv"
OUT_FILE = ROOT / "data" / "quotes.csv"

HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
MAX_GROWTH = 0.20


def fetch_chart(symbol):
    """Renvoie (cours, [(date, montant), ...]) pour un symbole Yahoo. Lève une exception en cas d'échec."""
    last_error = None
    for attempt in range(2):
        host = HOSTS[attempt % len(HOSTS)]
        url = (
            f"https://{host}/v8/finance/chart/{urllib.parse.quote(symbol)}"
            "?range=5y&interval=1mo&events=div"
        )
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                payload = json.load(resp)
            result = (payload.get("chart") or {}).get("result")
            if not result:
                err = (payload.get("chart") or {}).get("error") or {}
                raise ValueError(err.get("description") or "symbole introuvable")
            result = result[0]
            price = result.get("meta", {}).get("regularMarketPrice")
            if price is None:
                raise ValueError("pas de cours")
            raw = (result.get("events") or {}).get("dividends") or {}
            dividends = [
                (datetime.fromtimestamp(d["date"], tz=timezone.utc).date(), float(d["amount"]))
                for d in raw.values()
            ]
            return float(price), dividends
        except urllib.error.HTTPError as e:
            last_error = e
            if e.code == 404:
                break  # inutile de réessayer
            time.sleep(2)
        except Exception as e:  # réseau, JSON, symbole…
            last_error = e
            time.sleep(2)
    raise RuntimeError(str(last_error))


def estimate(dividends, today):
    """Renvoie (dividendes de l'année en cours, prévision de l'année suivante), par action."""
    year = today.year
    by_year = {}
    for d, amount in dividends:
        by_year[d.year] = by_year.get(d.year, 0.0) + amount
    this_year = by_year.get(year, 0.0)

    trailing = sum(a for d, a in dividends if today - timedelta(days=365) < d <= today)

    complete = [(y, by_year[y]) for y in range(year - 3, year) if by_year.get(y, 0.0) > 0]
    growth = 0.0
    if len(complete) >= 2:
        (y0, d0), (y1, d1) = complete[0], complete[-1]
        growth = (d1 / d0) ** (1.0 / (y1 - y0)) - 1.0
        growth = max(-MAX_GROWTH, min(MAX_GROWTH, growth))

    return this_year, trailing * (1.0 + growth)


def fmt(value):
    """Nombre avec point décimal, sans zéros inutiles (format lu par l'application)."""
    return f"{value:.4f}".rstrip("0").rstrip(".") or "0"


def main():
    today = datetime.now(timezone.utc).date()
    with open(TICKERS_FILE, newline="", encoding="utf-8") as f:
        tickers = [r for r in csv.DictReader(f) if (r.get("ticker") or "").strip()]

    rows, ok, failed = [], 0, []
    for t in tickers:
        ticker = t["ticker"].strip()
        name = (t.get("name") or "").strip()
        symbol = (t.get("yahoo") or "").strip() or f"{ticker}.PA"
        try:
            price, dividends = fetch_chart(symbol)
            this_year, forecast = estimate(dividends, today)
            rows.append([ticker, name, fmt(price), fmt(this_year), fmt(forecast)])
            ok += 1
        except Exception as e:
            print(f"ECHEC {ticker} ({symbol}) : {e}", flush=True)
            rows.append([ticker, name, "", "", ""])
            failed.append(ticker)
            # Si les 5 premiers titres échouent tous, Yahoo bloque : inutile d'insister.
            if ok == 0 and len(failed) >= 5:
                print(
                    "ARRET : les 5 premiers titres ont échoué. Yahoo Finance refuse probablement "
                    "les requêtes venant de GitHub (erreur 403/429) ou n'est pas joignable. "
                    "quotes.csv n'est pas modifié.",
                    flush=True,
                )
                return 1
        time.sleep(0.7)  # on ménage le service

    print(f"{ok} titre(s) récupéré(s), {len(failed)} en échec" + (f" : {', '.join(failed)}" if failed else ""))
    if ok == 0:
        print("Aucun titre récupéré : quotes.csv n'est pas modifié.", file=sys.stderr)
        return 1

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["ticker", "name", "price", "dividend2026", "forecast2027"])
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
