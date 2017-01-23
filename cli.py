from scrapy import cmdline

cmdline.execute("scrapy runspider vn_poem\\spiders\\tkaraoke.py -o vn_poem\\data\\data.jl -t jsonlines".split())

