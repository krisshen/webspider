# -*- coding: utf-8 -*-
import scrapy

class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']
    allowed_domains = ['www.trademe.co.nz']
    start_urls = ['https://www.trademe.co.nz/property/residential-property-for-sale/southland/catlins/view-list']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        self.logger.info('response code: %s', response.status)
        # self.logger.info('response headers: %s', response.headers)
        # self.logger.info('first author: %s', response.selector.xpath("//small[@itemprop='author']/text()").getall())
        self.logger.info('titles: %s', response.selector.xpath("//*[@class='tmp-search-card-list-view__title ']/text()").getall())
        self.logger.info('titles: %s', response.selector.xpath("//*[@class='tmp-search-card-list-view__content-body']/text()").getall())
