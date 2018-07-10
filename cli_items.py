from scrapy import cmdline
import os

if __name__ == '__main__':
    cmdline.execute("scrapy runspider site/spiders/items.py -o site/raw_data/hosocongty.jl -t jsonlines".split())

# debug
# cmdline.execute("scrapy runspider vn_news\\spiders\\baomoi_article.py -o vn_news\\raw_data\\data.jl -t jsonlines".split())
# cmdline.execute("scrapy runspider vn_news\\spiders\\baomoi_recrawl.py -o vn_news\\raw_data\\data.jl -t jsonlines".split())

