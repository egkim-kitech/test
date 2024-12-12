from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["Kitech", "airflow_test"]
) as dag:
    def select_fruit():
        fruit = ["APPLE", "ORANGE", "GRAPE"]
        random_fruit = random.choice(fruit)
        print(f"Today's fruit is {random_fruit}")
        
    # make select vegitable
    def select_vegitable():
        vegitable = ["TOMATO", "CUCUMBER", "ONION"]
        random_vegitable = random.choice(vegitable)
        print(f"Today's vegitable is {random_vegitable}")

    t1 = PythonOperator(
        task_id="t1",
        python_callable=select_fruit,
    )

    t2 = PythonOperator(
        task_id="t2",
        python_callable=select_vegitable,
    )

    t1 >> t2