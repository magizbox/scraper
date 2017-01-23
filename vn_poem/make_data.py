import json
import os

import pandas as pd

jsonlines_file = "raw_data\\data.jl"
lines = open(jsonlines_file).readlines()
poems = [json.loads(line) for line in lines]
df = pd.DataFrame(poems)
authors = list(df["author"].unique())
authors = [author.lower() for author in authors]
data_folder = "data"
previous_authors = os.listdir(unicode(data_folder))
# create author folder
for author in authors:
    if author not in previous_authors:
        os.mkdir(os.path.join(data_folder, author))
# create poem folder
for poem in poems:
    author = poem["author"].lower()
    title = poem["title"]
    title = title.replace("*", "")
    title = title.replace(".", "")
    text = poem["text"]
    filepath = os.path.join(data_folder, author, title + ".txt")
    if not os.path.exists(filepath):
        open(filepath, "wb").write(text.encode("utf-8"))
