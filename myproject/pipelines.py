# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        # for header in item['headers']:
        #     header = header.strip()
        #     if 'location' in header.lower():
        #         item['location']
        for i, header in enumerate(item['headers']):
            currentHeader = header.strip().lower()
            currentValue = item['values'][i]
            if 'location' in currentHeader:
                item['location'] = currentValue
            # if 'rooms' in header:
            #     item['rooms'] = currentValue
            # if 'property type' in header:
            #     item['propertyType'] = currentValue
            # if 'floor area' in header:
            #     item['floorArea'] = currentValue
            # if 'land area' in header:
            #     item['landArea'] = currentValue
            # if 'price' in header:
            #     item['price'] = currentValue
            # if 'parking' in header:
            #     item['parking'] = currentValue

        spider.logger.info("location: %s", item['location'].strip())
        # spider.logger.info("rooms: %s", item['rooms'].strip())
        # spider.logger.info("propertyType: %s", item['propertyType'].strip())
        # spider.logger.info("floorArea: %s", item['floorArea'].strip())
        # spider.logger.info("landArea: %s", item['landArea'].strip())
        # spider.logger.info("price: %s", item['price'].strip())
        # spider.logger.info("parking: %s", item['parking'].strip())
       
        return item