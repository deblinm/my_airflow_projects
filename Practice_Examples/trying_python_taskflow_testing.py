from airflow.decorators import dag, task
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args = {
    'owner' : 'deblin',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=1)
}

@dag("Taskflow_Opeator",default_args=default_args,start_date=datetime(2025,1,1),schedule="@daily" )

def hello_world_etl():


    @task()
    def get_name():
        return "Deblin"

    @task()
    def get_age():
        return 39

    @task()
    def greet(name,age):
        print(f"Hello! My name is {name} and I am {age} years old.")


    name=get_name()
    age=get_age()
    greet(name=name,age=age)    