import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "CMYK19SHCFNA5IEY"
NEWS_API_KEY = "e30beeb6fe6f48319c6675f097b31668"

# Twilio API Keys.
ACCOUNT_SID = "ACfbf6a87f61a91c812fc45d6bb00f4df7"
AUTH_TOKEN = "MY AUTH KEY"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]


# Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = data_list[1]["4. close"]


# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


news_params = {
    "apiKey" : NEWS_API_KEY,
    "q": STOCK_NAME
}
# If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 0:
    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = news_response.json()["articles"][:3]
    # Use Python slice operator to create a list that contains the first 3 articles. Hint:

    # Create a new list of the first 3 articles' headline and description using list comprehension.
    articles_list = [f"{STOCK_NAME}: {up_down}{diff_percent}%. \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(articles_list)

    # Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in articles_list:
        message = client.messages.create(
            body=article,
            from_="+19894398341",
            to="+971589196282"
        )
