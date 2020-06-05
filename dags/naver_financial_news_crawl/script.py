import ginaleo
from datetime import date
from ginaleo.crawler.news_crawl_machine import NewsCrawlMachine
from ginaleo.data.naver_news_post_process import PostProcess
from ginaleo.crawler.top500_crawler import Top500

n_comp = 50
max_page = 10
as_of = date.today().strftime('%Y-%m-%d') 
crawl_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/tmp'
in_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/tmp'
out_path = '/usr/local/airflow/dags/naver_financial_news_crawl/data/naver_news'

top500 = Top500(True, '/usr/local/airflow/dags/naver_financial_news_crawl')
comp = top500.company_list

print (comp )
ncm = NewsCrawlMachine(crawl_path)
ncm.execute(as_of, as_of, comp[:n_comp], max_page)

ps = PostProcess(in_path, out_path)
ps.execute(as_of, comp[:n_comp])