# 只抓晚上有開的店(if == "-") [中午有沒有開不管]
#  抓晚上最底限的價錢: "￥20,000～￥29,999" -> '20000'
# 幫我把 <= 10000 抓出來, 存成另外一個csv
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
page = 50
# PD!
c = ["分數", "日文", "英文", "網站", "價錢"]
df = pd.DataFrame(columns=c)
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print(url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("好像是最後一頁了")
        break
    html = BeautifulSoup(response)

    restaurants = html.find_all("li", class_="list-rst")
    for r in restaurants:
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        rating = r.find("b", class_="c-rating__val")
        prices = r.find_all("span", class_="c-rating__val")
        # HW
        print(prices[0].text)

        if prices[0].text == "-":
            price_dinner = None
        elif prices[0].text.startswith("～"):
            price_dinner = (int(prices[0].text.split("～")[1]
                                .replace("￥", "")
                                .replace(",", "")))
        else:
            price_dinner = (int(prices[0].text.split("～")[0]
                                          .replace("￥", "")
                                          .replace(",", "")))
        if not price_dinner is None and price_dinner <= 10000:
            print(rating.text, prices[0].text,
                  prices[1].text,en.text,
                  ja.text, en["href"])
            # PD!!
            data = [en["href"], ja.text, en.text, rating.text, price_dinner]
            s = pd.Series(data, index=["網站", "日文", "英文", "分數", "價錢"])

            df = df.append(s, ignore_index=True)
    page = page + 1
# PD!!
df.to_csv("tabelog.csv", encoding="utf-8", index=False)