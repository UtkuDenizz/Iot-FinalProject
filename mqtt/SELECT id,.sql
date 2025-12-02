SELECT id,
       device_id,
       temperature,
       humidity,
       "timestamp"
FROM public.sensor_data
LIMIT 1000;