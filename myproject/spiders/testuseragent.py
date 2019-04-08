# -*- coding: utf-8 -*-
import scrapy


class TestuseragentSpider(scrapy.Spider):
    name = 'testuseragent'
    allowed_domains = ['helloacm.com']
    start_urls = ['http://helloacm.com/api/user-agent']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        self.logger.info('response code: %s', response.status)
        self.logger.info('response code: %s', response.body)
        self.logger.info('response headers: %s', response.headers)
