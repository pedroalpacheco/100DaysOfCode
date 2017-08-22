# -*- coding: utf-8 -*-
import scrapy


class ImoveisSpider(scrapy.Spider):
    name = "imoveis"
    #allowed_domains = ["sc.olx.com.br/imoveis/"]
    #allowed_domains = ["sc.olx.com.br/imoveis?q=blumenau"]
    allowed_domains = ["sc.olx.com.br"]
    start_urls = (
        'http://sc.olx.com.br/imoveis?q=blumenau',
    )

    def parse(self, response):
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        self.log(response.url)
