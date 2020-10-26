# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from datetime import datetime


class ZdmSpidersMySQLPipeline(object):
    def __init__(self, host, port, db, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            port = crawler.settings.get('MYSQL_PORT'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            db = crawler.settings.get('MYSQL_DB'),
        )
    
    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host = self.host,
            port = self.port,
            db = self.db,
            user = self.user,
            password = self.password,
            charset = 'utf8mb4'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute("INSERT INTO product(product_name, user_name, user_comment, create_time) VALUES (%s, %s, %s, %s)", (item['product_name'], item['user_name'], item['user_comment'], create_time))
            self.connect.commit()
        except Exception as e:
            print(e)

        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()