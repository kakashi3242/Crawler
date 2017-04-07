# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    module = scrapy.Field()
    title = scrapy.Field()
    note = scrapy.Field()
    more = scrapy.Field() 
    content = scrapy.Field()
