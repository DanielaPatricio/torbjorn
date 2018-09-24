# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IkeaProduct(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    itemid = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    size = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()


