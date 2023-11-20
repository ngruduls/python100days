import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "Content-Type": "text",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-platform": "Windows",
    "Accept-Language": "en-GB,en;q=0.9,lv-LV;q=0.8,lv;q=0.7,en-US;q=0.6"
}

response = requests.get(URL)
website_html = response.text
#print(website_html)

soup = BeautifulSoup(website_html, 'lxml')

# item_prices = soup.select("tr td span")
item_prices = soup.find_all("span", class_="a-offscreen")
print(len(item_prices))
item_price = item_prices[0].getText()
price_without_currency = item_price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)