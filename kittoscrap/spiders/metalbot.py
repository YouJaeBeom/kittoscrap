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
        metalitem = KittoscrapItem()
        metalitem['Time_now'] = Time
        metalitem['Platinum'] = float(Platinum)
        metalitem['Palladium'] = float(Palladium)
        metalitem['Rhodium'] = float(Rhodium)
        items.append(metalitem)
        print("Time => ", Time)
        print("Platinum => ", metalitem['Platinum'])
        print("Palladium => ", metalitem['Palladium'])
        print("Rhodium => ", metalitem['Rhodium'])
        return items



   
