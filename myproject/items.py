# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PropertyCard(scrapy.Item):
    title = scrapy.Field()
    detail = scrapy.Field()
    listedDate = scrapy.Field()
    footer = scrapy.Field()

class Property(scrapy.Item):
    headers = scrapy.Field()
    values = scrapy.Field()
    listingId = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    listedDate = scrapy.Field()
    location = scrapy.Field()
    rooms = scrapy.Field()
    propertyType = scrapy.Field()
    floorArea = scrapy.Field()
    landArea = scrapy.Field()
    price = scrapy.Field()
    parking = scrapy.Field()
    description = scrapy.Field()