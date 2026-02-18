CREATE OR REPLACE VIEW mv_env_analytics AS
WITH calendar AS (
    SELECT *
    FROM generate_series(
        (SELECT MIN(ts_utc) FROM my_env_hourly),
        (SELECT MAX(ts_utc) FROM my_env_hourly),
        INTERVAL 1 HOUR
    ) AS t(ts_utc)
),

grid AS (
    SELECT
        c.ts_utc,
        l.place_id
    FROM calendar c
    CROSS JOIN dim_location l
),

joined AS (
    SELECT
        g.place_id,
        g.ts_utc,
        e.temp_c,
        e.wind_ms,
        e.pm10,
        e.pm2_5,
        e.ozone,
        e.uv_index,
        e.name as city_name
    FROM grid g
    LEFT JOIN my_env_hourly e
      ON g.place_id = e.place_id
     AND g.ts_utc  = e.ts_utc
)

SELECT
    j.*,

    -- fill missing values
    COALESCE(j.temp_c,0)  AS temp_c_filled,
    COALESCE(j.pm2_5,0)   AS pm2_5_filled,

    -- 24hr rolling averages
    AVG(j.temp_c) OVER (
        PARTITION BY j.place_id
        ORDER BY j.ts_utc
        ROWS BETWEEN 23 PRECEDING AND CURRENT ROW
    ) AS temp_24hr_avg,

    AVG(j.pm2_5) OVER (
        PARTITION BY j.place_id
        ORDER BY j.ts_utc
        ROWS BETWEEN 23 PRECEDING AND CURRENT ROW
    ) AS pm25_24hr_avg,

    -- conditional KPI
    CASE
        WHEN j.temp_c > 35 AND j.pm2_5 > 25
        THEN 1 ELSE 0
    END AS hot_hazy_flag

FROM joined j;
