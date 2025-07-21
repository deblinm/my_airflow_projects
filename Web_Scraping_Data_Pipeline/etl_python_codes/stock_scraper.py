import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from get_ticker_data import tickers_data

def scrape_stock_prices (ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.prettify())



