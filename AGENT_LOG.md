# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-08: Bar chart of median sale price by city

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then add a horizontal bar chart of the median sale price for each city above the table on index.html. Keep the table and the $10,000 rule as they are." Then: "do it again this time"
- **Agent produced:** The agent first found that index.html was still the placeholder page, with no table and no $10,000 rule, so it stopped and proposed a plan instead of guessing. After approval it added `scripts/city_medians.py`, which writes `data/city_median_prices.json` (sales of $10,000 or more only). It replaced `index.html` with a page showing a horizontal bar chart of the 18 city medians, a table of the same numbers under it, and a note stating the $10,000 rule.
- **Checked or changed:** The agent recomputed the medians from the SQLite file. At a $1,000 cutoff they match the description sheet (Ann Arbor $571,000), and at $10,000 they match the script (Ann Arbor $572,000). Its first phone layout cut off city names and pushed values off the screen. It caught this in a screenshot and moved the names above the bars on narrow screens.

## 2026-11-08: Redesign index.html in the style of a reference page

- **Asked:** (with a screenshot of a reference page; prompt written in Chinese, translated here) "Make the web page follow the format of this example from the professor, with a more polished and complete interface and title. The wording can be a little different, and the colors can change too."
- **Agent produced:** A new look for `index.html`: a dark navy header band with a small label, a large title and an intro line; four headline numbers (cities, sales counted, highest and lowest median); the price rule in a highlighted box; the bar chart and the table each in their own card; a Rank column in the table. All numbers still come from `data/city_median_prices.json`.
- **Checked or changed:** The agent took screenshots at desktop width, phone width and in dark mode. Its first version had the headline numbers stuck to the bottom of the header, and on a phone the table was too wide and cut off its last column. It fixed both and checked again.

## 2026-11-08: Finish the README

- **Asked:** "now finish the README FILE in my repo"
- **Agent produced:** Filled in every README section: the site's title, its question and audience, the live site link, fuller data notes (the price rule, how the medians are defined, and what the site does with each of the "Five things that will bite you"), and the tools used. It removed the "Start here" section, as the template says to, and the "Who did what" section, after asking whether I worked alone.
- **Checked or changed:** The agent recounted the 31 sales over $5,000,000 from the CSV before stating it. It could not open the live site from its environment to confirm the link works, so I need to check that link myself.
