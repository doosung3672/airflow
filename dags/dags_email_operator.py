from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 1, 29, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = BashOperator(
      task_id='send_email_task'",
      to = 'doosungkang@naver.com',
      cc = 'doosungkang@hanmail.net',
      subject ='airflow 성공메일',
      html_content = 'airflow 작업이 완료되었습니다.'
    )