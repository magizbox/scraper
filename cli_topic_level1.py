from scrapy import cmdline
from config import DATA_FOLDER
import os

if __name__ == '__main__':
    file = "{}/topic_level1.jl".format(DATA_FOLDER)
    try:
        os.remove(file)
    except:
        pass
    command = "scrapy runspider website/spiders/topic_level1.py -o {} -t jsonlines".format(file)
    cmdline.execute(command.split())
