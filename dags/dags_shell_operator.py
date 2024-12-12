from __future__ import annotations
import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_shell_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["Kitech", "airflow_test"]
) as dag:
    t1 = BashOperator(task_id="t1",bash_command="pwd")
    
    t2 = BashOperator(
        task_id="t2",
        bash_command="/opt/airflow/plugins/select_fruit.sh APPLE",
    )

    t1 >> t2
