import re
from scrapy.spiders import CrawlSpider
# from os.path import join, dirname
import json



def urls():
    for i in range(1600000, 1700000):
        # yield "http://www.hosocongty.vn/a-com-68.htm"
        yield "http://www.hosocongty.vn/a-com-{}.htm".format(i)


class ItemSpider(CrawlSpider):
    name = "hosocongty"

    start_urls = urls()

    def parse(self, response):
        url = response.url
        name = response.css(".news_subject::text").extract_first()
        mst = response.css(".companyDetail p:contains('Mã số thuế') strong a::text").extract_first()
        address = response.css(".companyDetail p:contains('Địa chỉ') strong::text").extract_first()
        closed_text = response.css(".companyDetail span:contains('Đã đóng mã số thuế')::text").extract()
        status = "deactive" if len(closed_text) > 0 else "active"
        bank_info = response.css(".companyDetail p:contains('Số TK') strong::text").extract()
        try:
            license_number = response.css(".companyDetail li:contains('Giấy phép kinh doanh') a::text").extract_first()
        except Exception as e:
            print("Cannot parse license_number")
            license_number = ""
        try:
            start_date = response.css(".companyDetail li:contains('Giấy phép kinh doanh')::text").extract()[1]
            start_date = re.search(r"\d+\/\d+/\d+", start_date).group()
        except Exception as e:
            print("Cannot parse date")
            start_date = ""
        ceo = response.css(".companyDetail li:contains('Giám đốc') a::text").extract_first()
        phone_numbers = response.css(".companyDetail li:contains('Điện thoại:') strong::text").extract()
        phone_numbers = [phone for phone in phone_numbers if phone not in "hide"]
        category_names = response.css(".box_content table tr td:nth-child(2) a::text").extract()
        category_ids = response.css(".box_content table tr td:nth-child(3)::text").extract()[1:]
        categories = list(zip(category_names, category_ids))
        yield {
            "url": url,
            "name": name,
            "mst": mst,
            "address": address,
            "bank_info": bank_info,
            "status": status,
            "license_number": license_number,
            "start_date": start_date,
            "ceo": ceo,
            "phone_numbers": phone_numbers,
            "categories": categories
        }
