import re

from os.path import join
from scrapy.spiders import CrawlSpider
import scrapy


class BaomoiArticleSpider(CrawlSpider):
    name = "baomoi"
    # allowed_domains = ["http://poem.tkaraoke.com/"]

    folder = "D:/PycharmProjects/crawl_vn_news/vn_news"
    filepath = join(folder, "pipelines", "crawled_urls.txt")
    start_urls = [line.strip() for line in open(filepath, "r").readlines()]

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        url = response.url
        id = re.compile(".*/(\d+).epi").match(url).groups()[0]
        content = response.css(".sapo ::text").extract_first()
        body_text = response.css(".body-text")
        for text in body_text:
            text_content = text.css("::text").extract()
            if type(text_content) == list:
                text_content = u"".join(text_content)
            content += text_content + " "

        title = response.css("h1 ::text").extract_first()
        yield {"url": url, "id": id, "title": title, "content": content}
