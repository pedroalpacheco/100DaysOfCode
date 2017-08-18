# -*- coding: utf-8 -*-
import scrapy


class OblumenauSpider(scrapy.Spider):
    name = "oblumenau"
    start_urls = (
        'http://www.oblumenauense.com.br/site/',
    )

    def parse(self, response):
        divs = response.xpath('/html/body/div[2]/div/div/div[1]/section[5]/div[2]/div[1]/article')
        for div in divs:
            link = div.xpath('.//a').extract_first()
            yield {
                'link':link,
            }


