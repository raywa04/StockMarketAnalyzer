from pyspark.sql import SparkSession
import requests
import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO)

ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'  # Replace with your actual API key

def fetch_stock_data(symbol):
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact'
    response = requests.get(api_url)
    data = response.json()
    if "Time Series (Daily)" in data:
        df = pd.DataFrame(data["Time Series (Daily)"]).T
        df = df.reset_index().rename(columns={
            'index': 'date',
            '1. open': 'open',
            '2. high': 'high',
            '3. low': 'low',
            '4. close': 'close',
            '5. adjusted close': 'adjusted_close',
            '6. volume': 'volume',
            '7. dividend amount': 'dividend_amount',
            '8. split coefficient': 'split_coefficient'
        })
        return df
    else:
        logging.error(f"Failed to fetch data for {symbol}: {data.get('Note', 'Unknown error')}")
        return pd.DataFrame()

def process_data(df, symbol):
    spark = SparkSession.builder.appName("StockDataProcessing").getOrCreate()
    spark_df = spark.createDataFrame(df)
    processed_df = spark_df.filter(spark_df['close'] > 0)
    os.makedirs('data', exist_ok=True)
    processed_df.toPandas().to_csv(f'data/{symbol}_data.csv', index=False)
    spark.stop()

if __name__ == "__main__":
    symbol = "AAPL"
    df = fetch_stock_data(symbol)
    if not df.empty:
        process_data(df, symbol)
