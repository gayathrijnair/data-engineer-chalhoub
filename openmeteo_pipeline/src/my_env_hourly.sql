CREATE OR REPLACE VIEW my_env_hourly AS
WITH
    weath AS (SELECT * FROM fct_weather),
    air   AS (SELECT * FROM fct_air),
    loc   AS (SELECT * FROM dim_location)

SELECT *
place_id,
coalesce (weath.ts_utc, air.ts_utc) as ts_utc,
temp_c,
wind_ms,
pm10,
pm2_5,
ozone,
uv_index,
name,
country,
lat,
lon,
timezone,
elevation_m
FROM weath
FULL JOIN air
  ON weath.ts_utc = air.ts_utc
 AND weath.place_id = air.place_id
LEFT JOIN loc
  ON weath.place_id = loc.place_id;