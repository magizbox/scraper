python vn_news/pipelines/pre_crawl.py
scrapy runspider vn_news/spiders/baomoi.py -o vn_news/raw_data/data.jl -t jsonlines --set HTTPCACHE_ENABLED=0
python vn_news/pipelines/process_data.py
git add -A
git commit -m "update data"
git push origin master