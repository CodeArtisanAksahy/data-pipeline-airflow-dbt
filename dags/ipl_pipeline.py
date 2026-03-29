
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'akshaythakur',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ipl_pipeline',
    default_args=default_args,
    description='Daily IPL analytics pipeline on Snowflake',
    schedule_interval=None,
    start_date=datetime(2026, 3, 29),
    catchup=False,
) as dag:

    run_stg = BashOperator(
        task_id='run_stg_ipl_matches',
        bash_command='echo "Running stg_ipl_matches..."',
    )

    run_team = BashOperator(
        task_id='run_fct_team_performance',
        bash_command='echo "Running fct_team_performance..."',
    )

    run_venue = BashOperator(
        task_id='run_fct_venue_stats',
        bash_command='echo "Running fct_venue_stats..."',
    )

    test_data = BashOperator(
        task_id='test_data',
        bash_command='echo "Running dbt tests..."',
    )

    send_alert = BashOperator(
        task_id='send_alert',
        bash_command='echo "IPL pipeline completed successfully!"',
    )

   