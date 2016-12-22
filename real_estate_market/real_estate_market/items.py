# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RemHouseInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    type = scrapy.Field()
    floor = scrapy.Field()
    direction = scrapy.Field()
    metro = scrapy.Field()
    neighbourhood = scrapy.Field()
    district = scrapy.Field()
    block = scrapy.Field()
    time = scrapy.Field()
    uri = scrapy.Field()
