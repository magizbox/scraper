import pandas as pd
import json

with open("../raw_data/data.jl") as f:
    items = f.read().splitlines()
items = [json.loads(item) for item in items]
df = pd.DataFrame(items)
counter = df.groupby("job").count().reset_index().sort_values("name", ascending=False)
counter["count"] = counter["name"]
del counter["url"]
del counter["name"]
counter.to_excel("../tmp/analysis.xlsx", index=False)
print(counter)