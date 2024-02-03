from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python  import PythonOperator
from common.common_func  import regist

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 1, 31, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    regist_t1 = PythonOperator (
       task_id="regist_t1",
       python_callable=regist,
       op_args=['doosung','man','kr','incheon']
    )


    regist_t1