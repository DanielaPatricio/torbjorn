# -*- coding: utf-8 -*-
import scrapy
from torbjorn.products import IkeaProduct
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector


class ProductsSpider2(scrapy.Spider):
    name = 'productsspider2'
    allowed_domains = ['ikea.com']
    start_urls = ['https://www.ikea.com/pt/pt/catalog/allproducts/department/']

    def parse(self,response):
        links = response.xpath('//div[contains(@ class,"productCategoryContainer ")]/ul/li/a/@href').extract()
        i = 1
        for link in links:
            abs_url = response.urljoin(link)
            #url_next = '//div[contains(@ class,"productCategoryContainer ")]['+str(i)+']/ul/li/a/@href'
            if (i <= len(links)):
                i = i + 1
                yield scrapy.Request(abs_url, callback = self.parse_indetail)


    def parse_indetail(self, response):
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
            item['category'] = response.xpath('//title/text()').extract()
            yield item

