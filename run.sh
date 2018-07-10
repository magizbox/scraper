export TMP_FOLDER=/data/tmp/hosocongty
source activate scraper && scrapy runspider site/spiders/items.py -o $TMP_FOLDER/data.jl -t jsonlines --set HTTPCACHE_ENABLED=0