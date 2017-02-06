python vn_news/pipelines/pre_crawl.py
scrapy runspider vn_news/spiders/baomoi.py -o vn_news/raw_data/data.jl -t jsonlines
python vn_news/pipelines/process_data.py
