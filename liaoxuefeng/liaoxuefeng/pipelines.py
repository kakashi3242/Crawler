# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.htmlfrom
# scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
import time
import pymysql
import pymysql.cursors
import socket
import select
import sys
import os
import errno

# 连接数据库,类名要跟settings里面设置的名字一致
class MySQLStorePipeline(object):
    # 数据库配置
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('pymysql',
                                            db='crawler',
                                            user='root',
                                            passwd='123456',
                                            cursorclass=pymysql.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )
    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    # 将每行写入数据库中
    def _conditional_insert(self, tx, item):
        tx.execute('INSERT INTO liaoxuefeng (title, href) VALUES (%s, %s)',
                    (item['title'], item['href']))
