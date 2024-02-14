from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python  import PythonOperator
from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator

with DAG(
    dag_id="dags_seoul_api_corona",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 2, 13, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    ''' 서울시 코로나19 확진자 발생동향'''
    tb_corona19_count_status= SeoulApiToCsvOperator(
        task_id ='tb_corona19_count_status',
        dataset_nm ='tbCorona19CountStatus',
        path='/opt/airflow/files/tbCorona19CountStatus/{{data_interval_end.in_timezon("Asia/Seoul") |ds_nodash}}',
        file_name = 'TbCorona19CountStatus.csv'
    )

    ''' 서울시 코로나19 백신 예방접종 현황 '''
    tv_corona19_vaccine_stat_new = SeoulApiToCsvOperator(
        task_id ='tv_corona19_vaccine_stat_new',
        dataset_nm ='tvCorona19VaccinestatNew',
        path='/opt/airflow/files/tvCorona19VaccinestatNew/{{data_interval_end.in_timezon("Asia/Seoul") |ds_nodash}}',
        file_name = 'tvCorona19VaccinestatNew.csv'        
    )

    tb_corona19_count_status >> tv_corona19_vaccine_stat_new

