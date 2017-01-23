from scrapy import cmdline

cmdline.execute("scrapy runspider crawl_vn_poems\\spiders\\tkaraoke.py -o data.jl -t jsonlines".split())

