# scripts/extract_unique_tickers.py

import json
import csv

INPUT = "data/sampled/10k_sample.jsonl"
OUTPUT = "data/ticker_to_sector_partial.csv"

unique_tickers = set()
with open(INPUT, "r", encoding="utf-8") as fin:
    for line in fin:
        rec = json.loads(line)
        for t in rec.get("tickers", []):
            unique_tickers.add(t.upper().strip())

# Write out CSV with header: ticker (and blank sector for now)
with open(OUTPUT, "w", newline="", encoding="utf-8") as fout:
    writer = csv.writer(fout)
    writer.writerow(["ticker", "sector"])
    for t in sorted(unique_tickers):
        writer.writerow([t, ""])
print(f"Wrote {len(unique_tickers)} unique tickers to {OUTPUT}")
