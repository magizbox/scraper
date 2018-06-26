import re
from scrapy.spiders import CrawlSpider
from os.path import join, dirname
import json

DATA_FOLDER = join(dirname(dirname(dirname(__file__))), "nguoinoitieng", "raw_data")

class ItemSpider(CrawlSpider):
    name = "nguoinoitieng"
    join(dirname(__file__))
    f = open(join(DATA_FOLDER, "data_20180626.jl"))
    items = f.read().splitlines()
    items = [json.loads(item) for item in items]
    start_urls = [
        item["url"] for item in items
    ]

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        name = response.css(".motangan h2::text").extract_first()
        job = response.css(".brc a::text")[1].extract()
        birthday = response.css(".thongtin-right p:contains('Ngày sinh') a::text").extract()
        birthday = "-".join(birthday)
        location = response.css(".thongtin-right p:contains('Nơi sinh') a::text").extract_first()
        facebook = response.css(".motangan p:contains('Facebook') a::attr('href')").extract_first()
        email = response.css(".motangan p:contains('Email')::text").extract_first()
        phone = response.css(".motangan p:contains('Số điện thoại')::text").extract_first()
        url = response.url
        yield {
            "url": url,
            "name": name,
            "job": job,
            "birthday": birthday,
            "location": location,
            "facebook": facebook,
            "email": email,
            "phone": phone
        }
