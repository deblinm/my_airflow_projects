from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime


def_args = {
           "owner" : "airflow",
           "start_date" : datetime(2023,1,1)
           }


with DAG ("ETL_PIPELINE",
          catchup= False,
          default_args= def_args) as dag:
    
    start= EmptyOperator(task_id = "Start")
    e= EmptyOperator(task_id = "Extract")
    t= EmptyOperator(task_id = "Transform")
    l= EmptyOperator(task_id = "Load")
    end= EmptyOperator(task_id = "End")


    start >> e >> t >> l >> end

