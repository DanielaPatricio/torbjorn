# -*- coding: utf-8 -*-
import scrapy
from torbjorn.categories import IkeaCategory

class CategoriesSpider(scrapy.Spider):
    name = 'categoriesspider'
    allowed_domains = ['ikea.com']
    start_urls = ['https://www.ikea.com/pt/pt/catalog/allproducts/department/']

    def parse(self, response):
        for sel in response.xpath('//div[contains(@ class,"productCategoryContainer ")]/ul/li/a'):
            item = IkeaCategory()
            item['name'] = sel.xpath('normalize-space(text())').extract()
            item['link'] = "https://www.ikea.com" + sel.xpath('@href').extract_first()
            yield item
