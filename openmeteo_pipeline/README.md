# Open-Meteo Pipeline — Starter Skeleton

A minimal ETL pipeline skeleton using the [Open-Meteo](https://open-meteo.com/) free APIs.

> **Note:** This is intentionally barebones — it's a starting point, not a finished product.
> Your task is to extend it to meet the full [Case Study](../Case%20Study.md) requirements.

## Structure

```
src/
├── pipeline.py      # Main entry point — orchestrates extract → transform → load
├── extract.py       # API calls (geocoding, forecast, air quality)
├── transform.py     # Normalization & merging of raw API responses
└── load.py          # Write DataFrames to DuckDB
tests/
└── test_imports.py  # Smoke test — extend with your own tests
```

## Quick Start

```bash
pip install -r requirements.txt
python src/pipeline.py
```

## What's Included

- **Geocoding** lookup (city name → lat/lon) via Open-Meteo
- **Forecast** hourly temperature extraction
- **Air Quality** hourly PM2.5 extraction
- Basic DuckDB table creation and row insertion

## What's Missing (for you to build)

- [ ] Full data model (`dim_location`, `fct_weather`, `fct_air`, `mv_env_hourly`)
- [ ] Watermark / incremental ingestion logic
- [ ] Elevation enrichment
- [ ] Additional weather & air-quality variables (humidity, wind, PM10, ozone, UV)
- [ ] Raw JSON storage for replay/debug
- [ ] Config-driven cities, endpoints, DB URL (YAML/ENV)
- [ ] Logging and error handling with retries
- [ ] SQL DDL with window functions, conditional KPIs, gap handling
- [ ] Meaningful tests (watermark logic, transformations)
- [ ] Design documentation
