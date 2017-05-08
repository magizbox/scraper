from os.path import join

from os import listdir

folder = "D:/PycharmProjects/crawl_vn_news/vn_news"

data_folder = join(folder, "data")
files = listdir(data_folder)
ids = [f.split(".")[0] for f in files]
urls = ["http://www.baomoi.com/a/c/%s.epi" % id for id in ids]
open("crawled_urls.txt", "w").write("\n".join(urls))
