from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'akshay',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dbt_taxi_pipeline',
    default_args=default_args,
    description='Runs the dbt taxi data pipeline daily',
    schedule_interval='0 8 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    dbt_seed = BashOperator(
        task_id='dbt_seed',
        bash_command='cd /Users/akshaythakur/my_pipeline && dbt seed',
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /Users/akshaythakur/my_pipeline && dbt run',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /Users/akshaythakur/my_pipeline && dbt test',
    )

    dbt_seed >> dbt_run >> dbt_test