from selenium.webdriver import Chrome
import time
from pytube import Playlist
import os

driver = Chrome("./chromedriver")

driver.get("https://www.youtube.com/view_all_playlists")
driver.find_element_by_id("identifierId").send_keys("!!!!!")
driver.find_element_by_id("identifierNext").click()
time.sleep(5)

driver.find_element_by_class_name("whsOnd").send_keys("!!!!")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

ps = driver.find_elements_by_class_name("vm-video-title-text")
for p in ps:
    # 特徵: bs["href"] -> get_attribute("href")
    print(p.text)
    purl = p.get_attribute("href")
    print(purl)
    pl = Playlist(purl, suppress_exception=True)
    dirname = "yt/" + p.text + "/"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    try:
        pl.download_all(dirname)
    # 針對403先略過去
    except:
        print("略過", purl)

time.sleep(3)
driver.close()