# -*- coding: utf-8 -*-
import re
from scrapy.spiders import CrawlSpider
import scrapy

from nguoinoitieng.spiders.item import ItemSpider


class CategorySpider(CrawlSpider):
    name = "nguoinoitieng"
    dates_init = [
        (1, 31), (2, 29), (3, 31), (4, 30), (5, 31), (6, 30),
        (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)
    ]
    dates = []
    for date in dates_init:
        month, days = date
        for day in range(1, days + 1):
            dates.append("{}-{}".format(day, month))

    start_urls = [
        # "http://nguoinoitieng.tv/sinh-ngay/1-1"
        "http://nguoinoitieng.tv/sinh-ngay/{}/".format(date) for date in dates
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

        # for item in items:
        #     try:
        #         url = item.css(".tennnt::attr('href')").extract_first()
        #         url = response.urljoin(url)
        #         # yield {"url": url}
        #     except:
        #         pass

