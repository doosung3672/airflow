from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 29, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    var_value = Variable.get("sample_key")

    bash_var_1 = BashOperator(
        task_id="bash_var_1",
        bash_command=f"echo variable:{var_value}"
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_var_1 >> bash_t2
