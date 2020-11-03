#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess
import time
import schedule



# crawling start
def crawling_start():
    subprocess.call(['scrapy', 'crawl', 'metalbot'])

# 환율 start
def crawling_do():
    subprocess.call(['python', 'usd.py'])

schedule.every(1).minutes.do(crawling_start) #
#schedule.every().day.at("10:30").do(crawling_do) #
schedule.every(1).minutes.do(crawling_do) #30분마다 실행

#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)


        







