# scripts/fill_sectors_yfinance.py

import pandas as pd
import yfinance as yf

INPUT = "data/ticker_to_sector_partial.csv"
OUTPUT = "data/ticker_to_sector_yf.csv"  # partially filled

df = pd.read_csv(INPUT)
# Add a new column “sector_filled”
sectors = []
for idx, row in df.iterrows():
    t = row["ticker"]
    try:
        info = yf.Ticker(t).info
        sector = info.get("sector")
        if sector is None or sector == "":
            sector = ""
    except Exception as e:
        sector = ""
    sectors.append(sector)
    print(f"{t} → {sector}")

df["sector"] = sectors
df.to_csv(OUTPUT, index=False)
print(f"Saved partial sectors to {OUTPUT}")
