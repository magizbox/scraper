# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider
import scrapy

from website.spiders.items import ItemSpider


class CategorySpider(CrawlSpider):
    name = "nguoinoitieng"
    congiaps = [
        "ty", "suu", "dan", "mao", "thin", "ti",
        "ngo", "mui", "than", "dau", "tuat", "hoi"
    ]

    start_urls = [
        "http://nguoinoitieng.tv/con-giap/{}".format(congiap) for congiap in congiaps
    ]
    item_parser = ItemSpider()

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        items = response.css('.list-ngaymai div')
        for item in items:
            name = item.css(".tennnt::text").extract_first()
            job = item.css(".nsnnt::text").extract_first()
            url = item.css(".tennnt::attr('href')").extract_first()
            url = response.urljoin(url)
            yield {"name": name, "job": job, "url": url}
        try:
            next_url = response.css('.pagenumber a:contains("Tiếp")::attr("href")').extract_first()
            next_url = response.urljoin(next_url)

            yield scrapy.Request(next_url, callback=self.parse)
        except:
            pass
