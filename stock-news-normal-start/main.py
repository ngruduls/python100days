import datetime
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_api_key = "M0P1TGYZOK2ZNWEW"
news_api_key = "f024d95885f34ae094a15d8ec0891b31"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
dt_today = datetime.date.today()
dt_yesterday = dt_today - datetime.timedelta(days=1)
print(dt_yesterday)
dt_1_before_yesterday = dt_yesterday - datetime.timedelta(days=1)
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : "M0P1TGYZOK2ZNWEW"
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())
response.raise_for_status()
stock_data = response.json()
data = response.json()["Time Series (Daily)"]
print(data)

daily_prices_dict = stock_data.get("Time Series (Daily)")
print(daily_prices_dict)
prices_last_two = []

data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print("yesterday closing price: " + yesterday_closing_price)

for (key, value) in daily_prices_dict.items():
    if key == str(dt_yesterday):
        prices_last_two.append(float(value["4. close"]))
    if key == str(dt_1_before_yesterday):
        prices_last_two.append(float(value["4. close"]))
print(prices_last_two)

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
yesterday_closing_price = prices_last_two[0]
day_before_yesterday_closing_price = prices_last_two[1]
diff = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

price_diff = abs(yesterday_closing_price - day_before_yesterday_closing_price)
print(price_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((price_diff / yesterday_closing_price) * 100)
print("percent diff: " + str(diff_percent))

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 2:
    print("Get News")
    news_params = {
        "qInTitle": "Tesla",
        "apiKey": news_api_key
    }
    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()
    data = response.json()
    print(data)

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = data["articles"][:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    #TODO 9. - Send each article as a separate message via Twilio.
    account_sid = 'ACed633f5511e4a7de1bcdbe8652b6a4f3'
    auth_token = '9c2fd612f6f64d44520bef2590aeac10'
    client = Client(account_sid, auth_token)

    for article in formatted_articles[:2]:
        message = client.messages.create(
            from_='+12562865552',
            body=article,
            to='+37128375730'
        )

        print(message.sid)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

