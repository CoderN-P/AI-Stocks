from pynytimes import NYTAPI
from dotenv import load_dotenv
import os
import datetime
load_dotenv()



# Create an instance of the API class
nyt = NYTAPI(os.environ['NYT_KEY'], parse_dates=True)
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
options = {
    "sort": "newest",  # Sort by oldest options
    # Return articles from the following four sources
    "sources": [
        "New York Times",
        "AP",
        "Reuters",
        "International Herald Tribune"
    ],
    # Only get information from the Politics desk
    "news_desk": [
        "Stocks"
    ],
    # Headline should contain "bill", "costs over", or "victory"
    "headline": [
        "stock"
    ]
}

articles = nyt.article_search(query='Apple', dates={'begin':yesterday, 'end':today}, options=options, results=10)
print(articles)
for article in articles:
    print(article['headline']['main'])
    print(article['pub_date'])
    print(article['web_url'])
    print()

