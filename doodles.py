import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen, urlretrieve
import json
import os
years = ["2019"]
# HW
result = []
for y in years:
    for m in range(12):
        url = "https://www.google.com/doodles/json/" + str(y) + "/" + str(m + 1) + "?hl=zh_TW"
        print(url)
        response = urlopen(url)
        doodles = json.load(response)
        for d in doodles:
            url = "https:" + d["url"]
            print(d["title"], url)
            dirname = "doodles/" + str(y) + "/" + str(m + 1) + "/"
            path = dirname + url.split("/")[-1]
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            urlretrieve(url, path)
            # HW
            doodle = {"title":d["title"],
                      "path":path,
                      "url":url,
                      "type":url.split(".")[-1],
                      "year":int(y),
                      "month":int(m)}
            result.append(doodle)
# HW
f = open("doodles.json", "w", encoding="utf-8")
json.dump(result, f)
f.close()