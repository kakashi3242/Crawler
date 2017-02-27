import scrapy
from liaoxuefeng.items import LiaoxuefengItem


class liaoxuefengSpider(scrapy.Spider):
    
    name = 'liaoxuefeng'
    allowed_domain = ['liaoxuefeng.com']
    start_urls = [
        'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    ]

    def parse(self, response):
        navigation = '//*[@id="main"]/div[3]/div[2]/div/div[1]/div[2]/ul[2]/li'
        for navi in response.xpath(navigation):
            item = LiaoxuefengItem()
            item['title'] = navi.xpath('a/text()').extract()
            item['href'] = navi.xpath('a/@href').extract()
            yield item