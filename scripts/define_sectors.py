# scripts/define_sectors.py

# These 11 sector names match the GICS standard.
SECTOR_LIST = [
    "Technology",
    "Energy",
    "Financials",
    "Consumer Discretionary",
    "Consumer Staples",
    "Health Care",
    "Industrials",
    "Materials",
    "Real Estate",
    "Utilities",
    "Communication Services"
]


def print_sectors():
    print("Your 11 sectors are:")
    for idx, s in enumerate(SECTOR_LIST):
        print(f"  {idx}: {s}")


if __name__ == "__main__":
    print_sectors()
