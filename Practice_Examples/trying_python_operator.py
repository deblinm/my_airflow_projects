from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {

    'owner' : 'deblin',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=1)
}

def greet(name,age):
    print(f"Hey!!! I am {name} and I am {age} years old")

with DAG ("Python_Operator_Testing",
    default_args=default_args,
    start_date=datetime(2025,1,1),
    schedule="@daily"
 )       as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={'name':'Tom', 'age':20}
    )

    task1