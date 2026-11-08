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
