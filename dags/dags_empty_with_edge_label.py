from airflow import DAG
import datetime
import pendulum
import random
from airflow.operators.python import PythonOperator
from airflow.utils.edgemodifier import Label
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_empty_with_edge_label",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 2, 9, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    empty_1 = EmptyOperator(
        task_id ='empty_1'
    )    
    empty_2 = EmptyOperator(
        task_id ='empty_2'
    )
    empty_1 >> Label('1과2사이')>>empty_2

    empty_3 = EmptyOperator(
        task_id ='empty_3'
    )

    empty_4 = EmptyOperator(
        task_id ='empty_4'
    )    

    empty_5 = EmptyOperator(
        task_id ='empty_5'
    )    

    empty_6 = EmptyOperator(
        task_id ='empty_6'
    )

empty_2 >> Label('Start Branch') >> [empty_3,empty_4,empty_5]>>Label('End Branch')>>empty_6