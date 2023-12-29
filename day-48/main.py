from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open afteer program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

my_dict = {}
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery ul li time")
times_reformatted = []
for time in times:
    time_attribute = time.get_attribute("datetime")
    date = time_attribute.split("T")[0]
    times_reformatted.append(date)

locations = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .shrubbery ul li a")

for i in range(len(times)):
    my_dict[i] = {"time": times_reformatted[i], "name": locations[i].text}

print(my_dict)

#driver.close()
driver.quit()