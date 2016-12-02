# -*- coding: utf-8 -*-
import scrapy
import json

class RentSpider(scrapy.Spider):
    name = 'rent'

    start_urls = ['http://sz.lianjia.com/zufang/']

    def parse(self, response):
        # follow links to author pages
        for href in response.xpath('//div[@class="pic-panel"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_rent)

        # follow pagination links
        page_url = response.selector.xpath('//div[@class="page-box house-lst-page-box"]/@page-url').extract_first()
        page_data_jl = response.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract_first()
        page_data = json.loads(page_data_jl)
        next_page = page_data["curPage"]+1 
        if next_page <= page_data['totalPage']:
            next_page = page_url.replace('{page}',str(next_page))
        else:
            nextpage=None
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_rent(self, response):
        yield {
            'price': int(response.xpath('//span[@class="total"]/text()').extract_first()),
        }
