from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'akshaythakur',
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    'retry_exponential_backoff': True,
    'email_on_failure': True,
    'email_on_retry': False,
    'email': ['akshaythakur@gmail.com'],
}

with DAG(
    dag_id='taxi_pipeline',
    default_args=default_args,
    description='Daily taxi data pipeline',
    schedule_interval='17 17 * * *',
    start_date=datetime(2026, 3, 29),
    catchup=False,
    on_failure_callback=lambda context: print(f"DAG Failed! Task: {context['task_instance'].task_id}"),
    on_success_callback=lambda context: print(f"DAG Succeeded!"),
) as dag:

    load_data = BashOperator(
        task_id='load_data',
        bash_command='echo "Loading taxi data..."',
    )

    transform_data = BashOperator(
        task_id='transform_data',
        bash_command='echo "Transforming data with dbt..."',
    )

    test_data = BashOperator(
        task_id='test_data',
        bash_command='echo "Running dbt tests..."',
    )

    send_alert = BashOperator(
        task_id='send_alert',
        bash_command='echo "Pipeline completed successfully!"',
    )

    load_data >> transform_data >> test_data >> send_alert