from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task
from airflow.decorators import task_group
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


with DAG(
    dag_id="dags_python_with_task_group",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 2, 9, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def inner_func(**kwargs):
        msg = kwargs.get('msg')  or ''
        print(msg)

    with TaskGroup(group_id='second_group',tooltip='두번째 그룹입니다') as group_2:
         ''' 여기에 적은 docstring은 표시되지 않습니다. '''
         @task(task_id='inner_function1')
         def inner_func1(**kwargs):
                print('두번째 TaskGroup 내 첫번째 task입니다.')

         inner_function2 = PythonOperator(
                task_id='inner_function2',
                python_callable=inner_func,
                op_kwargs={'msg':'두번째 TaskGroup내 두번째 task입니다.'}
         )        
         inner_func1() >> inner_function2
    group_2




