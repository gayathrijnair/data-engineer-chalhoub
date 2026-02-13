# Data Engineer — Take-Home Case Study

Welcome! This repository contains a **take-home case study** for the Data Engineer position.

---

## 📋 Objective

Build a small, production-minded data product that:

1. Ingests hourly weather and hourly air-quality data for multiple cities from [Open-Meteo](https://open-meteo.com/) (no auth),
2. Saves raw and modelled data into a DB of your choice (local or cloud),
3. Produces join-ready tables and non-trivial SQL metrics,
4. Publishes a dashboard (Streamlit provided as an example; any BI is fine).

---

## 📡 Data Sources (choose at least these three per city)

- **Geocoding** (city → lat/lon, timezone)
- **Forecast (hourly)** (e.g., temperature, humidity, wind)
- **Air Quality (hourly)** (e.g., PM10, PM2.5, ozone, UV)
- **Elevation** (enrichment; static)

> *Optional bonus: Historical weather backfill for QA and gap-filling.*

---

## ⚙️ Functional Requirements

### Incrementality & Idempotency

- Maintain a watermark per endpoint & per city (e.g., max `ts_utc` processed).
- Each run only ingests new hours > watermark; re-runs are safe.

### Persistence

- Store raw JSON for replay/debug.
- Load normalised rows into your chosen DB (DuckDB/SQLite/Postgres/BigQuery/etc.).

### Data Model (minimum)

- `dim_location(place_id, name, country, lat, lon, timezone, elevation_m)`
- `fct_weather(place_id, ts_utc, temp_c, rh_pct, wind_ms)`
- `fct_air(place_id, ts_utc, pm10, pm2_5, ozone, uv_index)`
- Join view: `mv_env_hourly` = inner join on `(place_id, ts_utc)`

### Non-trivial SQL

- Use at least one **window function** (e.g., 24-hour rolling averages).
- Derive conditional KPIs (e.g., "hot & hazy hour" when `temp_c > 35` AND `pm2_5 > 25`).
- Handle missing hours using a date/hour calendar + left join + `COALESCE`.

### Dashboard (tool of your choice)

- **Filters:** City(ies), Date range
- **KPIs:** Median Temp, PM2.5 P95, Hot & Hazy Hours/day
- **Charts:** Hourly line(s) and daily bars; a small table for recent rows
- Must query the joined dataset (e.g., `mv_env_hourly`) from your DB.

---

## 🏗️ Engineering Quality

- Config-driven (YAML/ENV) endpoints, variables, cities, DB URL.
- Logging (at least INFO level), basic error handling & retries.
- Tests: unit test the watermark logic and at least one transformation.
- Docs: concise README with how to run, how to change DB, and design notes.

---

## 📂 Repository Structure

We provide two **starter skeletons** to save you boilerplate time. You are free to modify, extend, or replace them entirely.

```
├── openmeteo_pipeline/        # Starter ETL pipeline (Python + DuckDB)
│   ├── src/
│   │   ├── pipeline.py        # Main entry point
│   │   ├── extract.py         # API calls (geocoding, forecast, air quality)
│   │   ├── transform.py       # Normalization & merging
│   │   └── load.py            # Write to DuckDB
│   ├── tests/
│   │   └── test_imports.py    # Test skeleton — extend with your own tests
│   ├── requirements.txt
│   └── README.md
├── openmeteo_dashboard/       # Starter Streamlit dashboard
│   ├── app.py                 # Minimal Streamlit app
│   ├── requirements.txt
│   └── README.md
└── README.md                  # ← You are here
```

## 🚀 Getting Started

### Pipeline

```bash
cd openmeteo_pipeline
pip install -r requirements.txt
python src/pipeline.py
```

### Dashboard

```bash
cd openmeteo_dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## ✅ What We're Looking For

| Area                     | Expectation                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Correctness**          | Pipeline ingests data, models it correctly, dashboard displays it           |
| **Incrementality**       | Watermark-based ingestion; re-runs are safe and idempotent                  |
| **Data Modelling**       | `dim_location`, `fct_weather`, `fct_air`, `mv_env_hourly` (or equivalent)  |
| **SQL Skills**           | Window functions, conditional KPIs, calendar-based gap handling             |
| **Engineering Quality**  | Config-driven, logging, error handling, tests, clean code                   |
| **Documentation**        | README with run instructions, design notes, trade-offs, known limitations   |

---

## 📦 Deliverables

1. **ETL repo** with modular code (extract/normalise/load), SQL DDL, tests, and a state file for watermarks.
2. **Dashboard repo** (Streamlit provided as example; any reporting tool acceptable).
3. **README + short design note** (1–2 pages): incrementality, timezones, schema, trade-offs, and known limitations.
4. **Evidence of idempotency** (e.g., run logs or a note describing re-run behaviour).

---

## ✔️ Acceptance Criteria

- Pulls ≥ 2 cities; resolves via Geocoding; enriches Elevation.
- Ingests hourly Forecast and hourly Air Quality; loads to DB with upserts on `(place_id, ts_utc)`.
- Maintains per-endpoint watermarks; re-runs do not duplicate data.
- Exposes `mv_env_hourly` (joined hourly weather + air data) and supports the required KPIs & charts.
- Dashboard runs locally (or cloud) and reads from the chosen DB.

---

## ⏱️ Time Expectation

This is designed to be completable in **4–6 hours**. Focus on demonstrating solid engineering practices over pixel-perfect dashboards.

## 💬 Questions?

If anything in the case study is unclear, please don't hesitate to reach out. Good luck!
