# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TkaraokeSpider(scrapy.Spider):
    name = 'tkaraoke'
    # allowed_domains = ['tkaraoke.com']
    start_urls = ['http://poem.tkaraoke.com/']


    def parse(self, response):
        content = response.css("ul.ul-option-search li:nth-child(3) ::text").extract()[1]
        yield {"content": content}
