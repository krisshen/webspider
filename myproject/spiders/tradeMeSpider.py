# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TrademespiderSpider(CrawlSpider):
    name = 'tradeMeSpider'
    allowed_domains = ['www.trademe.co.nz']
    start_urls = ['https://www.trademe.co.nz/property/residential-property-for-sale/southland/catlins/view-list']

    rules = (
        Rule(LinkExtractor(allow=r'property/residential/sections-for-sale/auction-'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        self.logger.info("url: %s", response.url)
        self.logger.info("location: %s", response.xpath("//*[@id='ListingAttributes']/tbody/tr[1]/td/text()").get())
        
        yield scrapy.Request(response.urljoin(response.url))
