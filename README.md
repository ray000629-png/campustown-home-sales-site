# What a home costs in each college town

## What this site is for

**Question:** how much does a typical home sell for in each of the 18 cities and towns in the College-town home sales dataset, and how big is the gap between the most and least expensive?

**Audience:** students, families and university staff comparing college towns, for example someone moving for a degree or a job who wants a sense of local home prices.

The site is a single page. It shows four headline numbers, a horizontal bar chart of the median sale price in each city, and a ranked table of the same medians with the number of sales behind each one. Medians run from $889,000 in Davis, CA to $229,900 in Urbana, IL.

## Live site

https://ray000629-png.github.io/campustown-home-sales-site/

## Data notes

**Price rule:** every price figure leaves out the 40 sales under $10,000 (four are under $1,000, one is $0). They are not real market prices. 35,402 of the 35,442 rows are used.

**Median sale price by city** (the bar chart and the table on `index.html`): the median `sale_price` of the counted sales in each `city`. A median of an even number of sales is the average of the middle two, shown rounded to the dollar. These medians can differ slightly from the description sheet's table, which uses a $1,000 cutoff (for example, Ann Arbor is $572,000 here and $571,000 there).

**What the site does not use, and why** (from "Five things that will bite you" in `docs/data_description_sheet.md`):

- **Days on market:** not shown, so the blank list and contract dates do not affect anything on the site.
- **Street addresses:** never used to deduplicate. Every row is counted once by `listing_id`, so the State College condo units that share an address all stay in.
- **`home_type`:** not used, because it labels almost every row `SINGLE_FAMILY`, including condos.
- **Other impossible values** (0 sq ft homes, huge lots, a $1,000,000,000 tax bill): not used, because the site only uses `city`, `state` and `sale_price`.
- **Very high prices:** the 31 sales over $5,000,000 are kept. A median is not pulled up by a few extreme values the way an average is, so no upper cutoff is needed.

**City** means the `city` column as recorded, not the `university` column. Each city is listed with its `state`.

**How to remake the data file:** `python3 scripts/city_medians.py` reads `data/college_town_home_sales.csv` and writes `data/city_median_prices.json`, which the page loads. It uses only the Python standard library.

## Tools we used

- **Claude Code** (Anthropic's AI coding agent) wrote the page, the data script and the documentation. Each step is recorded in `AGENT_LOG.md`.
- **HTML, CSS and JavaScript**, with no libraries or framework. The bar chart is drawn with plain HTML and CSS.
- **Python 3** standard library (`csv`, `statistics`, `json`) for `scripts/city_medians.py`.
- **SQLite** (`data/college_town_home_sales.sqlite`) to check the medians a second way.
- **Playwright with Chromium**, used by the agent to screenshot the page at desktop and phone width and in dark mode.
- **GitHub Pages** to publish the site, through `.github/workflows/pages.yml`.

## Citation

College-town home sales dataset, version 1.0 (2026). University of Illinois-Deloitte Foundation Center for Business Emerging Technologies. Data collected March 2026.
