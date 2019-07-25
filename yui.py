import requests
from bs4 import BeautifulSoup
import json
import os
start = 0
while True:
    url = "https://www.google.com/search?ei=gXcUXcnrAYqvmAXZgIXgAg&yv=3&q=%E6%9E%97%E5%BF%97%E7%8E%B2&tbm=isch&vet=10ahUKEwiJsPLjmInjAhWKF6YKHVlAASwQuT0IYSgB.gXcUXcnrAYqvmAXZgIXgAg.i&ved=0ahUKEwiJsPLjmInjAhWKF6YKHVlAASwQuT0IYSgB&ijn=" + str(start) + "&start=" + str(100*start) + "&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc"
    headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    response = requests.get(url,headers = headers)
    # urlretrieve(url, "a.txt")
    html = BeautifulSoup(response.text)
    metas = html.find_all("div", class_="rg_meta")
    if len(metas) == 0:
        print("最後一頁")
        break
    for m in metas:
        picture = json.loads(m.text)
        img_url = picture["ou"]
        print(img_url)
        dirname = "chiling/"
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        fp = dirname + img_url.split("/")[-1]
        try:
            img_response = requests.get(img_url, headers=headers, stream=True)
        except:
            print("跳過:", img_url)
            continue
        try:
            f = open(fp, "wb")
            f.write(img_response.raw.read())
            f.close()
        except:
            print("放過")

    start = start + 1