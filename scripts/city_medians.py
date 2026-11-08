"""Write data/city_median_prices.json from data/college_town_home_sales.csv.

Rule: only sales of $10,000 or more are counted. The data description sheet
says 40 sales are under $10,000 (four under $1,000, one at $0), and those are
not real market prices.

Run from the repository root:  python3 scripts/city_medians.py
Uses only the Python standard library.
"""
import csv
import json
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_prices.json"
MIN_PRICE = 10_000

prices = defaultdict(list)
total_rows = 0
excluded = 0
# csv.DictReader keeps every value as text, so zipcode, county_fips and
# parcel_number keep their leading zeros. Only sale_price is converted.
with SOURCE.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        total_rows += 1
        price = int(row["sale_price"])
        if price < MIN_PRICE:
            excluded += 1
            continue
        prices[(row["city"], row["state"])].append(price)

cities = [
    {
        "city": city,
        "state": state,
        "sales": len(p),
        # A median of an even count can end in .5; keep whole numbers as ints.
        "median_price": (lambda m: int(m) if m == int(m) else m)(statistics.median(p)),
    }
    for (city, state), p in prices.items()
]
cities.sort(key=lambda c: c["median_price"], reverse=True)

result = {
    "source": "data/college_town_home_sales.csv",
    "rule": f"Sales under ${MIN_PRICE:,} are left out.",
    "min_price": MIN_PRICE,
    "total_rows": total_rows,
    "excluded_rows": excluded,
    "included_rows": total_rows - excluded,
    "cities": cities,
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT.relative_to(ROOT)}: {len(cities)} cities, "
      f"{total_rows - excluded} of {total_rows} rows, {excluded} excluded")
