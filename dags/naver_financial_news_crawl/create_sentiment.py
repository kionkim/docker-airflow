import ginaleo
from ginaleo.crawler.news_crawl_machine import NewsCrawlMachine
from ginaleo.data.create_sentiment_data import CreateSentimentData
from ginaleo.crawler.top500_crawler import Top500
from datetime import date, timedelta
import pandas as pd
import numpy as np
import pickle, json
from pathlib import Path
import pandas_datareader as pdr

n_comp = 50

yesterday = date.today() - timedelta(days = 1) 
as_of = yesterday.strftime('%Y-%m-%d') 

comp_list_path = '/usr/local/airflow/dags/naver_financial_news_crawl'
in_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/naver_news'
out_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/market_prediction'

top500 = Top500(True, comp_list_path)
comp = top500.company_list[:n_comp]
breakpoint = [1.03, 1.01, 0.99, 0.97]


cdsa = CreateSentimentData(in_path, out_path)
cdsa.process(as_of, comp, breakpoint)
