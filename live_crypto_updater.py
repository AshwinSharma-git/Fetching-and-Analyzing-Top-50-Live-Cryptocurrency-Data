import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import pandas as pd
import schedule
import time

# Step 1: Setup Google Sheets API Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\Ashwin sharma\Downloads\splendid-flow-450618-r0-adf2046ec467.json", scope)
client = gspread.authorize(creds)

# Step 2: Open the Google Sheet
sheet = client.open_by_key('1OYMd20wZhjniF1lf3UKyuw4lvCkv2zMcwW0ZfRUKt-w').sheet1

# Step 3: Function to Fetch and Update Data
def fetch_and_update():
    # Fetch data from CoinGecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Process data
    crypto_data = []
    for coin in data:
        crypto_data.append([
            coin['name'],
            coin['symbol'].upper(),
            coin['current_price'],
            coin['market_cap'],
            coin['total_volume'],
            coin['price_change_percentage_24h']
        ])

    # Clear existing data in the sheet
    sheet.clear()

    # Add headers and data to the sheet
    headers = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization', '24-hour Trading Volume', 'Price Change (24-hour %)']
    sheet.append_row(headers)

    for row in crypto_data:
        sheet.append_row(row)
    
    print("Sheet updated successfully!")

# Step 4: Schedule Updates Every 5 Minutes
schedule.every(5).minutes.do(fetch_and_update)

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)
