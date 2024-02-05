import pendulum
from airflow import DAG
from airflow.decorators import task
with DAG(
    dag_id="dags_python_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 2, 3, tz="Asia/Seoul"),
    catchup=True,
):
    @task(task_id="python_task")
    def show_template(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_template()