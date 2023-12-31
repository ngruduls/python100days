from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome browser open afteer program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, "")

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
timeout = time.time() + 60*5
last_saved_timestamp = time.time()

cookie = driver.find_element(By.ID, "cookie")
while True:
    highest_price_can_buy_ui_item = None
    if time.time() > timeout:
        break
    if int(time.time()) - int(last_saved_timestamp) == 5:
        last_saved_timestamp = time.time()
        money = driver.find_element(By.ID, "money").text
        money = float(money.strip().replace(",",""))
        print(money)

        #find all store elements
        store_elems = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in store_elems:
            print(item.text + "fails after this")
            price_elem = item.find_element(By.CSS_SELECTOR, "b")
            price_text = price_elem.text
            if len(price_text) > 0:
                price_split = price_text.split("-")
                price = float(price_split[1].strip().replace(",",""))
                print(price)
                if (price <= money) and (item.get_attribute("class") != "greyed"):
                    highest_price_can_buy_ui_item = item
        print(f"clicking on {highest_price_can_buy_ui_item.text} item\n")
        highest_price_can_buy_ui_item.click()
    cookie.click()

# driver.quit()