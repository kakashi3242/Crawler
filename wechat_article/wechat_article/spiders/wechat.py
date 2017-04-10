# -*- coding: utf-8 -*-
import scrapy
from wechat_article.items import WechatArticleItem


class WechatSpider(scrapy.Spider):
    name = "wechat"
    allowed_domains = ["vccoo.com"]
    start_urls = [
        'http://www.vccoo.com/hotarticle/?id=111',
        'http://www.vccoo.com/hotarticle/?id=129',
        'http://www.vccoo.com/hotarticle/?id=108',
        'http://www.vccoo.com/hotarticle/?id=130',
        'http://www.vccoo.com/hotarticle/?id=107',
        'http://www.vccoo.com/hotarticle/?id=103',
        'http://www.vccoo.com/hotarticle/?id=120',
        'http://www.vccoo.com/hotarticle/?id=123',
        'http://www.vccoo.com/hotarticle/?id=114',
        'http://www.vccoo.com/hotarticle/?id=132',
        'http://www.vccoo.com/hotarticle/?id=110',
        'http://www.vccoo.com/hotarticle/?id=109',
        'http://www.vccoo.com/hotarticle/?id=102',
        'http://www.vccoo.com/hotarticle/?id=101',
        'http://www.vccoo.com/hotarticle/?id=127',
        'http://www.vccoo.com/hotarticle/?id=104',
        'http://www.vccoo.com/hotarticle/?id=105',
        'http://www.vccoo.com/hotarticle/?id=119',
        'http://www.vccoo.com/hotarticle/?id=123',
        'http://www.vccoo.com/hotarticle/?id=106',
        'http://www.vccoo.com/hotarticle/?id=121',
        'http://www.vccoo.com/hotarticle/?id=128',
        'http://www.vccoo.com/hotarticle/?id=131',
        'http://www.vccoo.com/hotarticle/?id=133',
        'http://www.vccoo.com/hotarticle/?id=100',
    ]

    def parse(self, response):
        content = '//*[@id="main-cont-menu"]/li'
        item = WechatArticleItem()
        for con in response.xpath(content):
            item['artTitle'] = con.xpath("div[1]/div[2]/a/h3/text()").extract()
            item['artUrl'] = con.xpath('div[1]/div[2]/a/@href').extract()
            item['artAuthor'] = con.xpath(
                'div[1]/div[2]/div/a[2]/text()').extract()
            item['authUrl'] = con.xpath(
                'div[1]/div[2]/div/a[2]/@href').extract()
            read = con.xpath(
                'div[1]/div[2]/div/span[1]/text()').extract()[0]
            item['artRead'] = read.split(' ')[1]
            good = con.xpath(
                'div[1]/div[2]/div/span[2]/text()').extract()[0]
            item['artGood'] = good.split(' ')[1]
            item['artType'] = response.xpath(
                '//*[@id="header"]/div/div[2]/span/text()').extract()
            yield item

        nextPageIndex = response.xpath(
            '//*[@id="main-page"]/ul/li[1]/a/@href').extract()
        if nextPageIndex:
            curPage = int(nextPageIndex[0].split('=')[2]) + 1
        else:
            curPage = 1

        if curPage in range(1, 5):
            nextPage = response.xpath(
                '//*[@id="main-page"]/ul/li[10]/a/@href').extract()
        elif curPage in range(5, 97):
            nextPage = response.xpath(
                '//*[@id="main-page"]/ul/li[11]/a/@href').extract()
        elif curPage in range(97, 101):
            nextPage = response.xpath(
                '//*[@id="main-page"]/ul/li[9]/a/@href').extract()

        if nextPage:
            domain = 'http://www.vccoo.com'
            nextUrl = domain + nextPage[0]
            yield scrapy.http.Request(nextUrl, callback=self.parse)
