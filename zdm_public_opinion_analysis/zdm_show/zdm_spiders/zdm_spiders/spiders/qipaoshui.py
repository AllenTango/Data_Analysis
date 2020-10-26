# -*- coding: utf-8 -*-
import scrapy
from zdm_spiders.items import ZdmSpidersItem


class QipaoshuiSpider(scrapy.Spider):
    name = 'qipaoshui'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/qipaoshui/']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_ten)

    def parse_ten(self, response):
        products = response.xpath('//*[@id="feed-main-list"]/li')
        limit = 10
        for product in products:
            link = product.xpath('.//h5[@class="feed-block-title"]/a/@href').get()
            count = int(product.xpath('.//a[@class="z-group-data"]/span/text()').extract_first())
            if limit > 0 and count > 3:
                limit -= 1
                yield scrapy.Request(url=link, callback=self.prase_details)

    def prase_details(self, response):
        item = ZdmSpidersItem()
        item['product_name'] = ''.join(response.xpath('//*[@id="feed-main"]/div/div/div/h1[@class="title J_title"]/text()').extract_first().split())
        comments = response.xpath('//*[@class="comment_list"]')
        for comment in comments:
            item['user_name'] = comment.xpath('./div/div/a/span/text()').extract_first().strip()
            item['user_comment'] = comment.xpath('./div/div/div/p/span/text()').extract_first().strip()
            yield item
        page_down = response.xpath('//*[@id="commentTabBlockNew"]/ul/li[@class="pagedown"]/a/@href').extract_first()
        if page_down:
            yield scrapy.Request(page_down, callback=self.prase_details)