# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import DropItem

class EducsdnPipeline(object):
    def process_item(self, item, spider):
        if item['price'] == None:
            raise DropItem("drop item")
        else:
            return item

class MysqlPipeline(object):
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        # 自动调用；为了实例化当前类对象；cls就是当前这个类
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            user = crawler.settings.get("MYSQL_USER"),
            password = crawler.settings.get("MYSQL_PASS"),
            database = crawler.settings.get("MYSQL_DATABASE"),
            port = crawler.settings.get("MYSQL_PORT")

        )

    def open_spider(self, spider):
        '''负责连接数据库'''
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset="utf8", port=self.port)
        # 获取游标对象
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        '''执行数据表的写入操作'''
        sql = "insert into courses(title,url,pic,teacher,time,price) values('%s','%s','%s','%s','%s','%s')"%(item['title'],item['url'],item['pic'],item['teacher'],str(item['time']),str(item['price']))
        self.cursor.execute(sql)
        self.db.commit()
        return item


    def close_spider(self, spider):
        '''关闭连接数据库'''
        self.db.close()