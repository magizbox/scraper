import re
from scrapy.spiders import CrawlSpider


def urls():
    data = [
        "https://www.oxfordlearnersdictionaries.com/topic/animal_homes"
    ]
    return data


class TopicSpider(CrawlSpider):
    name = "topic"
    start_urls = urls()

    def parse(self, response):
        url = response.url
        topic_urls = response.css(".topic .list-col li a::attr('href')").extract()
        topic_names = response.css(".topic .list-col li a::text").extract()
        yield {
            "url": "https://www.oxfordlearnersdictionaries.com/topic/animal_homes",
            "name": "Animals"
        }
        for name, url in zip(topic_names, topic_urls):
            yield {
                "url": url,
                "name": name
            }