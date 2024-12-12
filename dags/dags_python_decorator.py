from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp
from airflow.decorators import task
import random

with DAG(
    dag_id="dags_python_decorator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["Kitech", "airflow_test"]
) as dag:
    
    @task(task_id="get_sftp")
    def get_sftp():
        print("get_sftp")
        
    python_task1 = get_sftp()