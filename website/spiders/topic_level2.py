import scrapy
from os.path import join
import json
from scrapy.spiders import CrawlSpider

from config import DATA_FOLDER


def urls():
    file = join(DATA_FOLDER, "topic_level1.jl")
    for item in open(file):
        data = item.strip()
        data = json.loads(data)
        yield data["url"]


class TopicSpider(CrawlSpider):
    name = "TOPIC_LEVEL_2"
    start_urls = urls()

    def parse(self, response):
        url = response.url
        topic = response.css(".webtop-g h2::text").extract_first()
        main_topic =  response.css("#main-topic-title::text").extract_first()
        words = response.css("ul.wordpool li a::text").extract()
        data =  {
            "url": url,
            "topic": topic,
            "main_topic": main_topic,
            "words": words
        }
        yield data
        topic_urls = response.css(".topic-explore .list-col li a::attr('href')").extract()
        for topic_url in topic_urls:
            yield scrapy.Request(topic_url, callback=self.parse)
