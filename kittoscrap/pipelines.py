# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class KittoscrapPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='117.17.189.6', user='root', password='samjung', database='samjung_test',port=3306)
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `비철금속시세` (`기준일`,`Platinum`,`Palladium`,`Rhodium`) VALUES (%s,%s,%s,%s)", (
                item['Time_now'].encode('utf-8'),
                item['Platinum'],
                item['Palladium'],
                item['Rhodium']))
            self.conn.commit()
            print("insert",item['Time_now'],item['Platinum'],item['Palladium'],item['Rhodium'])
        except Exception as e:
            print("Error", (e))
            return item

