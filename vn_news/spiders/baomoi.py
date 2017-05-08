# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider
import scrapy

from vn_news.spiders.baomoi_article import BaomoiArticleSpider


class BaomoiSpider(CrawlSpider):
    name = "baomoi"
    # allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = [
        "http://www.baomoi.com/feed.rss"
        "http://www.baomoi.com/xa-hoi.rss",
        "http://www.baomoi.com/the-gioi.rss",
        "http://www.baomoi.com/van-hoa.rss",
        "http://www.baomoi.com/kinh-te.rss",
        "http://www.baomoi.com/giao-duc.rss",
        "http://www.baomoi.com/the-thao.rss",
        "http://www.baomoi.com/giai-tri.rss",
        "http://www.baomoi.com/phap-luat.rss",
        "http://www.baomoi.com/khoa-hoc-cong-nghe.rss",
        "http://www.baomoi.com/doi-song.rss",
        "http://www.baomoi.com/xe-co.rss",
        "http://www.baomoi.com/nha-dat.rss"
    ]
    article_parser = BaomoiArticleSpider()

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        article_pages = response.xpath('//guid/text()').extract()
        for next_page in article_pages:
            yield scrapy.Request(response.urljoin(next_page), callback=self.article_parser.parse)

