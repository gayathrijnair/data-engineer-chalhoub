# Open-Meteo Dashboard — Starter Skeleton

A minimal [Streamlit](https://streamlit.io/) dashboard skeleton.

> **Note:** This is intentionally barebones — it's a starting point, not a finished product.
> Your task is to extend it to meet the full [Case Study](../Case%20Study.md) requirements.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## What's Included

- Basic Streamlit app with city filter and a line chart for temp/PM2.5
- DuckDB connection to read from the pipeline output

## What's Missing (for you to build)

- [ ] Connect to the proper DB / joined view (`mv_env_hourly`)
- [ ] Filters: City multi-select, date range picker
- [ ] KPI cards: Median Temp, PM2.5 P95, Hot & Hazy Hours/day
- [ ] Charts: Hourly line chart(s), daily bar chart(s)
- [ ] Table: Recent rows from the joined dataset
- [ ] Proper DB path configuration (not hardcoded)
- [ ] Any BI tool is acceptable — Streamlit is just a suggestion
