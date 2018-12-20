import re
from scrapy.spiders import CrawlSpider
# from os.path import join, dirname
import json



def urls():
    for i in range(1, int(1e6)):
        # yield "http://www.hosocongty.vn/a-com-68.htm"
        yield f"https://micro-services.vntrip.vn/search-engine/search/vntrip-hotel-availability/?hotel_ids={i}&check_in_date=20181220&nights=1"


class ItemSpider(CrawlSpider):
    name = "vntrip"

    start_urls = urls()

    def parse(self, response):
        url = response.url
        output = {}
        try:
            data = json.loads(response.text)["data"][0]
            output["name"] = data["name"]
            output["address"] = data["full_address"]
            output["url"] = url
        except:
            print("Error")
            output = {}
        # mst = response.css(".companyDetail p:contains('Mã số thuế') strong a::text").extract_first()
        # address = response.css(".companyDetail p:contains('Địa chỉ') strong::text").extract_first()
        # closed_text = response.css(".companyDetail span:contains('Đã đóng mã số thuế')::text").extract()
        # status = "deactive" if len(closed_text) > 0 else "active"
        # bank_info = response.css(".companyDetail p:contains('Số TK') strong::text").extract()
        # try:
        #     license_number = response.css(".companyDetail li:contains('Giấy phép kinh doanh') a::text").extract_first()
        # except Exception as e:
        #     print("Cannot parse license_number")
        #     license_number = ""
        # try:
        #     start_date = response.css(".companyDetail li:contains('Giấy phép kinh doanh')::text").extract()[1]
        #     start_date = re.search(r"\d+\/\d+/\d+", start_date).group()
        # except Exception as e:
        #     print("Cannot parse date")
        #     start_date = ""
        # ceo = response.css(".companyDetail li:contains('Giám đốc') a::text").extract_first()
        # phone_numbers = response.css(".companyDetail li:contains('Điện thoại:') strong::text").extract()
        # phone_numbers = [phone for phone in phone_numbers if phone not in "hide"]
        # category_names = response.css(".box_content table tr td:nth-child(2) a::text").extract()
        # category_ids = response.css(".box_content table tr td:nth-child(3)::text").extract()[1:]
        # categories = list(zip(category_names, category_ids))
        yield output
