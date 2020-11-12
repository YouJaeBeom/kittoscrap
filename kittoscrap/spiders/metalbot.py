# -*- coding: utf-8 -*-
from kittoscrap.items import KittoscrapItem
import json
import scrapy 
import json 
import time 
import re 
from datetime import datetime, timedelta 
import pymysql
import re
import urllib.request

class MetalbotSpider(scrapy.Spider):
    name = 'metalbot'
    allowed_domains = ['kitco.com']
    start_urls = ['http://www.kitco.com']

    def parse(self, response):
        items=[]

        Platinum = response.xpath('//*[@id="PT-bid"]/text()').extract_first()
        Palladium = response.xpath('//*[@id="PD-bid"]/text()').extract_first()
        Rhodium = response.xpath('//*[@id="RH-bid"]/text()').extract_first()
        now = datetime.now()
        Time = now.strftime('%Y-%m-%d %H:%M')

        # 환율 정보를 불러오는 라인
        page = urllib.request.urlopen(
            "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8")
        text = page.read().decode("utf8")
        # 시간 정보를 확인 합니다
        where = text.find('class="grp_info"> <em>')
        start_of_time = where + 22
        end_of_time = start_of_time + 16
        prin = text[start_of_time:end_of_time]

        # 달러
        usdwhere = text.find('<span>미국 <em>USD</em></span></a></th> <td><span>')
        usdletter = text[usdwhere + 48] + text[usdwhere + 50:usdwhere + 56]
        usdletter = float(usdletter)

        metalitem = KittoscrapItem()
        metalitem['Time_now'] = Time
        metalitem['Platinum'] = float(Platinum)*usdletter
        metalitem['Palladium'] = float(Palladium)*usdletter
        metalitem['Rhodium'] = float(Rhodium)*usdletter

        items.append(metalitem)
        print("Time => ", Time)
        print("Platinum => ", metalitem['Platinum'])
        print("Palladium => ", metalitem['Palladium'])
        print("Rhodium => ", metalitem['Rhodium'])
        return items



   
