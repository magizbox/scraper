# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy


class ListPoemSpider(CrawlSpider):
    name = "list_poem"
    # allowed_domains = ["http://poem.tkaraoke.com/"]
    start_urls = [
        # 'http://poem.tkaraoke.com/10102/Nguyen_Khuyen/',
        # 'http://poem.tkaraoke.com/10020/Tan_Da/',
        # 'http://poem.tkaraoke.com/10077/Ho_Xuan_Huong/',
        # 'http://poem.tkaraoke.com/10012/Xuan_Dieu/',
        'http://poem.tkaraoke.com/10163/Phan_Boi_Chau/',
        'http://poem.tkaraoke.com/10332/The_Lu/',
        'http://poem.tkaraoke.com/10005/Han_Mac_Tu/',
        'http://poem.tkaraoke.com/10022/Nguyen_Binh/',
        'http://poem.tkaraoke.com/10003/Huy_Can/',
        'http://poem.tkaraoke.com/10079/Che_Lan_Vien/',
        'http://poem.tkaraoke.com/11410/To_Huu/'
    ]

    def parse(self, response):
        self.logger.info('==> %s', response.url)
        pagination_pages = response.css('#SearchPaging a ::attr("href")').extract()
        for next_pagination_page in pagination_pages:
            yield scrapy.Request(response.urljoin(next_pagination_page), callback=self.parse)
        poem_pages = response.css('.td-poem-items a.a-name-poem ::attr("href")').extract()
        for poem_page in poem_pages:
            yield scrapy.Request(response.urljoin(poem_page), callback=self.parse_poem)

    def parse_poem(self, response):
        author = response.css(".a-name-poem ::text").extract_first()
        title = response.css(".h2-title-poem ::text").extract_first().strip()
        texts = response.css(".div-author-poem + div::text").extract()
        texts = u"\n".join([text.strip() for text in texts])
        yield {"author": author, "title": title, "text": texts}
        self.logger.info('==> %s', response.url)
