import json
import os
from os.path import dirname
import sys


class Article:
    def __init__(self, data):
        self.__dict__ = data

    def save(self, folder):
        filename = "%s.txt" % self.id
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(self.title.encode("utf-8"))
            f.write(self.content.encode("utf-8"))

if __name__ == '__main__':
    folder = dirname(dirname(sys.argv[0]))
    data_folder = os.path.join(folder, "data")
    js_files = os.path.join(folder, "raw_data", "data.jl")
    lines = open(js_files).readlines()

    articles = [Article(json.loads(line)) for line in lines]
    print "Crawled articles: %s" % len(articles)
    indexed_files = os.listdir(os.path.join(folder, "data"))
    indexed_articles = [f.split(".")[0] for f in indexed_files]
    new_articles = [article for article in articles if article.id not in indexed_articles]
    print "New articles    : %s" % len(new_articles)
    for article in new_articles:
        print "New article %s" % article.id
        article.save(data_folder)
