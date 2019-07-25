import requests
from bs4 import BeautifulSoup
import schedule
import time
from twilio.rest import Client


def job():
    response = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
    html = BeautifulSoup(response.text)
    rows = html.find("table").find("tbody").find_all("tr")
    for r in rows:
        tds = r.find_all("td")
        if "日圓" in tds[0].text:
            print("現金匯率:", tds[2].text)

            account_sid = "twilio帳號"
            auth_token = "twilio密碼"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to="要送去的電話號碼+886",
                from_="twilio電話號碼",
                body="日圓匯率:" + tds[2].text)

schedule.every().day.at("10:41").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)