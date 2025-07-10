from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {

    'owner' : 'deblin',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=1)
}

def get_name(ti):
    ti.xcom_push(key='first_name', value ='Deblin')
    ti.xcom_push(key='last_name', value ='Moitra')


def get_age(ti):
    ti.xcom_push(key='age', value = 39)    

def greet(ti):
    first_name= ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name= ti.xcom_pull(task_ids='get_name',key='last_name')
    age= ti.xcom_pull(task_ids='get_age',key='age')
    print(f"Hey!!! I am {first_name} {last_name} and I am {age} years old")


with DAG ("Python_XCOM_Operator_Testing",
    default_args=default_args,
    start_date=datetime(2025,1,1),
    schedule="@daily"
 )       as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet
    )
    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id="get_age",
        python_callable=get_age
    )

    [ task2, task3 ] >> task1