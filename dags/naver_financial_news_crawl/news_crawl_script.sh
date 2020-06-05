#!/bin/bash
echo "Script executed from: ${PWD}"

pip uninstall -y ginaleo

pip install git+https://kionkim:rlarldhs!1@github.com/kionkim/ginaleo.git

pip install -r /usr/local/airflow/dags/naver_financial_news_crawl/requirements.txt

# python script.py