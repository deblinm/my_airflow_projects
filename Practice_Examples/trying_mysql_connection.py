from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta

@dag(
    dag_id="example_sql_execute_query",
    start_date=datetime.now() + timedelta(days=-2),
    schedule=None,
    catchup=False,
    tags=['example'],
)
def example_dag():
    # Example SQL query
    sql_query = "SELECT * FROM sys.orchestration_api_detail"

    # Task to execute the query
    execute_query_task = SQLExecuteQueryOperator(
        task_id="execute_query",
        conn_id="my_sql_connection",
        sql=sql_query,
        parameters={"id": 123},
        autocommit=True
    )

    # Another task might use a different query or parameters
    # ...

    execute_query_task  # Define task dependencies if needed

dag_object = example_dag()