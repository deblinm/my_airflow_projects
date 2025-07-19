Summary: Stock prices web scraping project using Python and Airflow.

End to End ETL Pipeline :

Python Program 1 :
Step 1 : Read stock symbol data from SEC.gov
Step 2 : Dump the stock data in json format in minio s3 cloud bucket (google how to set up minio in our local machine,
            for windows it will be through docker or wsl)

Python Program 2 :

Step 1 : Read the stock symbol from minio cloud
Step 2:  For each symbol go to yahoo finance and pull its current day price
Step 3 : Load the data obtained in step 2 into a MySQL table.


Airflow jobs :

Call Python Program 1 -> Create a Sensor to sense file in Minio  -> Call Python Program 2 -> On SUccess Send a success email -> On Failure send a failure email


Technologies:
Python — For web scraping
Airflow — For scheduling and orchestration
BeautifulSoup / requests — To fetch and parse HTML
MySQL — To store stock price data
Minio -> For cloud experience