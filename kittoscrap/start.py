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
def crawling_pirce():
    subprocess.call(['python', 'usd.py'])

## 한국이 미국보다 14시간 빠름 14시에 크롤링 -> 시장 마지막 가격

schedule.every(60).minutes.do(crawling_start) # 1시간마다
schedule.every(60).minutes.do(crawling_pirce) # 1시간마다

#schedule.every().day.at("09:00").do(crawling_pirce) #

#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)


        







