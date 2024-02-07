from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 2, 07, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    @task(task_id ='dags_python_with_push_by_return')
    def xcom_push_result(**kwargs):
        retrun 'Success'

    @task(task_id ='dags_python_with_pull_1')
    def xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(task_ids"dags_python_with_push_by_return")
        print('xcom_pul 메소드로 직접 찾은 리턴 값'+value1)

    @task(task_id ='dags_python_with_pull_2')
    def xcom_pull_2(status,*kwargs):
        print('xcom_pul 메소드로 직접 찾은 리턴 값'+status)

    
    dags_python_with_push_by_return = xcom_push_result()
    xcom_pull_2(dags_python_with_push_by_return)
    dags_python_with_push_by_return >> xcom_pull_1()
