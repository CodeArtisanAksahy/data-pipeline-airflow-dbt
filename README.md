# Airflow Pipeline

An orchestrated data pipeline built with Apache Airflow and dbt.

## Pipeline Architecture
Airflow schedules and monitors the dbt pipeline daily.

## DAG: taxi_pipeline
load_data → transform_data → test_data → send_alert

## Features
- Automatic retries (3 retries with exponential backoff)
- Email alerts on failure
- Manual trigger support

## Tools Used
- Apache Airflow 2.9.0
- Docker
- dbt Core 1.11.7
- DuckDB

## How to Run
1. Install Docker
2. Run: docker compose up -d
3. Open: http://localhost:8080
4. Login: airflow/airflow
5. Trigger taxi_pipeline manually
