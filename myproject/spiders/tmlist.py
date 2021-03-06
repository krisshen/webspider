# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from myproject.items import Property

class TmlistSpider(scrapy.Spider):
    name = 'tmlist'
    allowed_domains = ['www.trademe.co.nz']
    start_urls = [
        'https://www.trademe.co.nz/property/residential-property-for-sale/waikato/waitomo',
        'https://www.trademe.co.nz/property/residential-property-for-sale/waikato/otorohanga',
        'https://www.trademe.co.nz/property/residential-property-for-sale/wellington/wellington'
        ]

    def parse(self, response):
        # titles = response.xpath("//*[@class='tmp-search-card-list-view__title ']/text()").getall()
        # self.logger.info('titles: %s', titles)
        # l = ItemLoader(item=PropertyCard(), response=response)
        # l.add_xpath('title', "//*[@class='tmp-search-card-list-view__title ']/text()")
        # propertyCard = l.load_item()
        # self.logger.info("result..........")
        # self.logger.info(propertyCard.get('title'))

        #
        # get each propertyCard's url, request it
        #
        for propertyCard in response.xpath("//*[@class='tmp-search-card-list-view__link']"):
            property = Property()
            propertyPageRelativeUrl = propertyCard.xpath('@href').extract_first()
            propertyPageFullUrl = response.urljoin(propertyPageRelativeUrl)
            # title = propertyCard.xpath(".//div[@class='tmp-search-card-list-view__title ']/text()").get(default=propertyCard.xpath(".//div[@class='tmp-search-card-list-view__title tmp-search-card-list-view__title--bold']/text()").get())
            # yield {
            #     'title': title,
            #     'propertyPageRelativeUrl': propertyPageRelativeUrl,
            #     'responseUrl:': propertyPageFullUrl
            # }
            # property['title'] = title
            property['link'] = propertyPageFullUrl
            yield scrapy.Request(url=propertyPageFullUrl, meta={'property': property}, callback=self.parsePropery)

        for propertyCard in response.xpath("//*[@class='tmp-search-card-top-tier__link']"):
            property = Property()
            propertyPageRelativeUrl = propertyCard.xpath('@href').extract_first()
            propertyPageFullUrl = response.urljoin(propertyPageRelativeUrl)
            # title = propertyCard.xpath(".//div[@class='tmp-search-card-top-tier__title ']/text()").get(default=propertyCard.xpath(".//div[@class='tmp-search-card-top-tier__title tmp-search-card-top-tier__title--bold']/text()").get())
            # yield {
            #     'title': title,
            #     'propertyPageRelativeUrl': propertyPageRelativeUrl,
            #     'responseUrl:': propertyPageFullUrl
            # }
            # property['title'] = title
            property['link'] = propertyPageFullUrl
            yield scrapy.Request(url=propertyPageFullUrl, meta={'property': property}, callback=self.parsePropery)

        #
        # get next page url, need to click 'Search' button first, pls refer middlewares.py
        #
        self.logger.info("next page is..............")
        nextPageRelativeUrl = response.xpath("//a[contains(@rel, 'next')]").xpath('@href').extract_first()
        nextPageFullUrl = response.urljoin(nextPageRelativeUrl)
        # yield {'nextPage': nextPageFullUrl}
        yield scrapy.Request(url=nextPageFullUrl, meta={'property': property}, callback=self.parse)

    def parsePropery(self, response):
        # response.xpath("").extract_first()
        
        property = response.meta['property']
        
        title = response.xpath("//*[@id='TitleContrainer']/div[2]/h1/text()").extract_first()
        listingId = response.xpath("//*[@id='ListingTitle_ListingNumberContainer']/text()").extract_first()
        listedDate = response.xpath("//*[@id='PriceSummaryDetails_ListedStatusText']/text()").extract_first()
        # location = response.xpath("//*[@id='ListingAttributes']/tbody/tr[1]/td/text()").extract_first()
        # rooms = response.xpath("//*[@id='ListingAttributes']/tbody/tr[2]/td/text()").extract_first()
        # propertyType = response.xpath("//*[@id='ListingAttributes']/tbody/tr[3]/td").extract_first()
        # floorArea = response.xpath("//*[@id='ListingAttributes']/tbody/tr[4]/td/text()").extract_first()
        # landArea = response.xpath("//*[@id='ListingAttribute']/tbody/tr[5]/td/text()").extract_first()
        # price = response.xpath("//*[@id='ListingAttributes']/tbody/tr[6]/td").extract_first()
        # parking = response.xpath("//*[@id='ListingAttributes']/tbody/tr[8]/td").extract_first()
        # description = response.xpath("//*[@id='ListingDescription_ListingDescription']/text()").extract_first()
        
        property['title'] = title
        property['listingId'] = listingId.replace('Listing #:', '').strip()
        property['listedDate'] = listedDate.replace('Listed: ', '').strip()
        # following attributes will be processed in pipelines.py
        property['location'] = ''
        property['rooms'] = ''
        property['propertyType'] = ''
        property['floorArea'] = ''
        property['landArea'] = ''
        property['price'] = ''
        property['parking'] = ''
        property['description'] = ''

        headers = response.xpath("//*[@id='ltHeaderRow']/text()").getall()
        values = response.xpath("//*[@id='ListingAttributes']/tbody/tr/td/text()").getall()
        cleanedValues = []
        for value in values:
            if value.strip() != '':
                cleanedValues.append(value)
        property['headers'] = headers
        property['values'] = cleanedValues

        #check open home times
        if 'Open home times' in headers[-1]:
            property['values'].append(response.xpath("//*[@id='open-homes']/div/button/span[1]/text()").extract_first())

        # yield {
        #     'header': headers,
        #     'values': values
        # }

        yield property