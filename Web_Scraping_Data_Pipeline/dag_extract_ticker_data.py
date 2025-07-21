import json

import sys
import os

# Append project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etl_python_codes.get_ticker_data import get_company_tickers

tickers_data = get_company_tickers()
with open("C:\\Users\debli\\airflow_tutorial_env\\SourceFiles\\company_tickers.json", "w") as f:
    json.dump(tickers_data, f)