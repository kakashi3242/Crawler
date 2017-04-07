# -*- coding: utf-8 -*-
import scrapy
from data.items import DataItem


class DataspiderSpider(scrapy.Spider):
    name = "dataSpider"
    allowed_domains = ["36dsj.com"]
    start_urls = [
        'http://www.36dsj.com/archives/category/ganhuo',
        ]

    def parse2(self,response):
        item = response.meta['item']

        item['content'] =  response.xpath('/html/body/section/div/div/article/p/text()').extract()

        return item

    def parse(self, response):
        content = '//div[@class="content"]/article'
        items = []
        for con in response.xpath(content):
            item = DataItem()
            item['module'] = response.xpath('//div[@class="content"]/h1/strong/a/text()').extract()
            item['title'] = con.xpath('h2/a/text()').extract()
            item['note'] = con.xpath(
                'p[@class="note"]/text()').extract()
            item['more'] = con.xpath(
                'p[@class="more"]/a/@href').extract()
            items.append(item)
            yield scrapy.http.Request(item['more'][0],meta={'item':item},callback=self.parse2)

            nextPage = response.xpath('//li[@class="next-page"]/a/@href').extract()
            if nextPage:
                next = nextPage[0]
                yield scrapy.http.Request(next,callback=self.parse)