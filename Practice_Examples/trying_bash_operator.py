
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {

    'owner' : 'deblin',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=1),
    'schedule_interval': '@daily'
}

with DAG ("Bash_Operator_Testing",
    default_args=default_args,
    start_date=datetime(2025,1,1)
 )       as dag:
        task1 = BashOperator (
                task_id='first_task',
                bash_command="echo hi, this is the first task"
        )
        task2 = BashOperator (
                task_id='second_task',
                bash_command="echo hi, this is the second task"
        )
        task3 = BashOperator (
                task_id='third_task',
                bash_command="echo hi, this is the third task"
        )


        task1 >> task2
        task1 >> task3




