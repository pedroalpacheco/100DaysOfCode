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
        next_page = response.xpath(
                '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
            )
        if next_page:
            self.log('Próxima Página: {}'.format(next_page.extract_first()))
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )

    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        tipo = response.xpath(
            '//span[contains(text(), "Tipo")]/following-sibling::strong/a/@title'
        ).extract_first()
        quartos = response.xpath(
            '//span[contains(text(), "Quartos")]/following-sibling::strong/text()'
        ).extract_first()
        yield {
            'title': title,
            'tipo': tipo,
            'quartos': quartos,
        }
