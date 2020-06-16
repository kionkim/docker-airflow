import ginaleo
from datetime import date, timedelta
from ginaleo.crawler.news_crawl_machine import NewsCrawlMachine
from ginaleo.data.naver_news_post_process import PostProcess
from ginaleo.crawler.top500_crawler import Top500

n_comp = 50
max_page = 10
yesterday = date.today() - timedelta(days = 1) 
as_of = yesterday.strftime('%Y-%m-%d') 
 
crawl_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/tmp'
in_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/tmp'
out_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/naver_news'
comp_list_path = '/usr/local/airflow/dags/naver_financial_news_crawl'

top500 = Top500(True, comp_list_path)
comp = top500.company_list

print (comp )
ncm = NewsCrawlMachine(crawl_path)
ncm.execute(as_of, as_of, comp[:n_comp], max_page)

ps = PostProcess(in_path, out_path)
ps.execute(as_of, comp[:n_comp])