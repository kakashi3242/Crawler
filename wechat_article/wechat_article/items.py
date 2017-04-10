# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WechatArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    artTitle = scrapy.Field()
    artAuthor = scrapy.Field()
    artRead = scrapy.Field()
    artGood = scrapy.Field()
    artUrl = scrapy.Field()
    authUrl = scrapy.Field()
    artType = scrapy.Field()
