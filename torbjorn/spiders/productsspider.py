# -*- coding: utf-8 -*-
import scrapy
from torbjorn.products import IkeaProduct

class ProductsSpider(scrapy.Spider):
    name = 'productsspider'
    allowed_domains = ['https://www.ikea.com/pt/pt']
    start_urls = ['https://www.ikea.com/pt/pt/catalog/categories/departments/pets/39570/']

    def parse(self, response):
        for sel in response.xpath('//div[contains(@ id,"item_")]'):
            item = IkeaProduct()
            item['itemid'] = str(sel.xpath('@id').extract()).split("_")[1]
            item['name'] = sel.xpath('.//span[contains(@ class,"productTitle ")]/text()').extract()
            item['description'] = sel.xpath('.//span[contains(@ class,"productDesp")]/text()').extract()
            item['price'] = sel.xpath('normalize-space(.//span[contains(@ class,"price regularPrice")]/text())').extract()
            item['unit'] = sel.xpath('.//span[contains(@ class,"unit")]/text()').extract()
            item['size'] = sel.xpath('normalize-space(.//span[contains(@ class,"size")]/text())').extract()
            item['image'] = "https://www.ikea.com" + sel.xpath('.//img/@ src').extract_first()
            item['link'] = "https://www.ikea.com" + sel.xpath('.//a/@ href').extract_first()

            yield item
