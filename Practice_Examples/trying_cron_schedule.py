
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {

    'owner' : 'deblin',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=1)
}

with DAG ("Schedule_With_Cron_expression_02",
    default_args=default_args,
    start_date=datetime(2025,1,1),
    schedule='00 16 * * Mon-Fri'
 )       as dag:
        task1 = BashOperator (
                task_id='first_task',
                bash_command="echo hi, this is the first task"
        )