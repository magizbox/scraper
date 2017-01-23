# -*- coding: utf-8 -*-
import scrapy


class ListPoemSpider(scrapy.Spider):
    name = "list_poem"
    allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = ['http://poem.tkaraoke.com/10020/Tan_Da/']

    def parse(self, response):
        pass
