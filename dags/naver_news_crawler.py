from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
# from airflow.operators.docker_operator import DockerOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 6, 1),
    "email": ["kion.kim@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('naver_news_crawler', default_args=default_args,
            schedule_interval='20 18 * * *',
            start_date=datetime(2020, 6, 1),
            catchup=False,
            description='Crawl and post-process naver news',
        )


# pip install git+https://kionkim:rlarldhs!1@github.com/kionkim/ginaleo.git


t1 = BashOperator(task_id="install_package", bash_command="./naver_financial_news_crawl/news_crawl_script.sh", dag=dag)


t2 = BashOperator(task_id="news_crawl", bash_command="python /usr/local/airflow/dags/naver_financial_news_crawl/script.py", dag=dag)

# crawling = PythonOperator(
#     task_id='news_crawl',
#     python_callable=callable,
#     dag=dag)


# crawling
t1 >> t2
# hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

# dummy_operator >> hello_operator
