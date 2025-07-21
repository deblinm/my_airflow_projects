import json
import requests
import boto3
from botocore.client import Config


minio_endpoint = "http://localhost:9000"
access_key = "myaccesskey"
secret_key = "mysecretkey"
bucket_name = "my-local-cloud"
object_name = "company_tickers.json"
local_file = "C:\\Users\debli\\airflow_tutorial_env\\SourceFiles\\company_tickers.json"

def get_company_tickers():
    """Connects to SEC.gov to retrieve the company_tickers.json file.
    Returns:
        dict: A dictionary containing company ticker information, or None if an error occurs.
    """
    url = "https://www.sec.gov/files/company_tickers.json"
    headers = {"User-Agent": "Your Name (Youremail@email.com)"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        company_data = response.json()

        if company_data:
            with open(local_file, "w") as f:
                json.dump(company_data, f)

            # Connect to MinIO
            s3 = boto3.client(
                's3',
                endpoint_url=minio_endpoint,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                config=Config(signature_version='s3v4'),
                region_name='us-east-1'
            )

            # Upload file
            s3.upload_file(local_file, bucket_name, object_name)

            print(f"Uploaded {local_file} to {bucket_name}/{object_name}")
        else:
            print("Failed to retrieve company ticker data.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from SEC.gov: {e}")
        return None


