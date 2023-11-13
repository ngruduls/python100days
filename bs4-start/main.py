from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
first_article = soup.find(class_="titleline")
first_article_text = first_article.find("a").string
print(first_article)
print(first_article_text)