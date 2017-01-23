from scrapy import cmdline

# cmdline.execute("scrapy runspider vn_poem\\spiders\\tkaraoke.py -o vn_poem\\data\\data.jl -t jsonlines".split())
cmdline.execute("scrapy runspider vn_poem\\spiders\\list_poem.py -o vn_poem\\raw_data\\data.jl -t jsonlines".split())

