import re
from scrapy.spiders import CrawlSpider
import scrapy


class BaomoiArticleSpider(CrawlSpider):
    name = "baomoi"
    # allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = [
        "http://www.baomoi.com/dong-nhi-show-hang-sieu-xe-audi-r8-13-ty-tai-sai-gon/c/21461403.epi",
    ]

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
