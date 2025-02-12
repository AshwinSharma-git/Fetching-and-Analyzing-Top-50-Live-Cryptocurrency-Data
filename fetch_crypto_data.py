import requests
import pandas as pd

# CoinGecko API URL
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',      # Get prices in USD
    'order': 'market_cap_desc', # Order by market cap
    'per_page': 50,            # Fetch top 50 cryptocurrencies
    'page': 1,
    'sparkline': 'false'       # No sparkline data
}

# Fetch data
response = requests.get(url, params=params)
data = response.json()

# Extract required fields
crypto_data = []
for coin in data:
    crypto_data.append({
        'Cryptocurrency Name': coin['name'],
        'Symbol': coin['symbol'].upper(),
        'Current Price (USD)': coin['current_price'],
        'Market Capitalization': coin['market_cap'],
        '24-hour Trading Volume': coin['total_volume'],
        'Price Change (24-hour %)': coin['price_change_percentage_24h']
    })

# Convert to DataFrame
df = pd.DataFrame(crypto_data)

# Save to Excel
df.to_excel('Top_50_Cryptocurrencies.xlsx', index=False)

print("Data fetched and saved to 'Top_50_Cryptocurrencies.xlsx'")
