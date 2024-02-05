from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2024, 2, 5, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    # START_DATE: 전월 말일, END_DATE:1일 전
    bash_task1 = BashOperator(
        task_id = 'bash_task1',
        env={'START_DATE':'{{data_interval_start.intimezone("Asia/Seoul") | ds }}',
             'END_DATE':'{{(data_interval_end.intimezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}'
        },
        bash_command='echo "START_DATE: $START_DATE && echo "END_DATE: $END_DATE"'
    )