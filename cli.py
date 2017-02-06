from scrapy import cmdline
import os

cmdline.execute("scrapy runspider vn_news\\spiders\\baomoi.py -o vn_news\\raw_data\\data.jl -t jsonlines".split())
