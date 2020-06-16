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
            schedule_interval='50 20 * * *',
            start_date=datetime(2020, 6, 1),
            catchup=False,
            description='Crawl and post-process naver news',
        )

t1 = BashOperator(task_id="refresh_package", 
                  bash_command="./naver_financial_news_crawl/refresh_package.sh", 
                  dag=dag)


t2 = BashOperator(task_id="news_crawl", 
                  bash_command="python /usr/local/airflow/dags/naver_financial_news_crawl/crawl_news.py", 
                  dag=dag)


t3 = BashOperator(task_id="create_sentiment", 
                  bash_command="python /usr/local/airflow/dags/naver_financial_news_crawl/create_sentiment.py", 
                  dag=dag)

# crawling = PythonOperator(
#     task_id='news_crawl',
#     python_callable=callable,
#     dag=dag)


# crawling
t1 >> t2 >> t3
# hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

# dummy_operator >> hello_operator
