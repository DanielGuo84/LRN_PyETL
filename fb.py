from selenium.webdriver import Chrome
import time
driver = Chrome("./chromedriver")

driver.get("https://www.facebook.com")

# bs: find, find_all
# selenium: find_element, find_elements
driver.find_element_by_id("email").send_keys()
driver.find_element_by_id("pass").send_keys()
driver.find_element_by_id("loginbutton").click()

s = input("請輸入安全碼")
driver.find_element_by_id("approvals_code").send_keys(s)
driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(1)
driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(5)
post = driver.find_element_by_class_name("userContent")
# 紙條: .text
print(post.text)

time.sleep(3)
driver.close()
