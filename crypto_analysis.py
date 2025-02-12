import pandas as pd

# Load the Excel file
file_path = 'Top_50_Cryptocurrencies.xlsx'
df = pd.read_excel(file_path)

# Verify column names
print(df.columns)

# 1. Identify the Top 5 Cryptocurrencies by Market Capitalization
top_5_by_market_cap = df.sort_values(by='Market Capitalization', ascending=False).head(5)

# 2. Calculate the Average Price of the Top 50 Cryptocurrencies
average_price = df['Current Price (USD)'].mean()

# 3. Analyze the Highest and Lowest 24-hour Percentage Price Change
highest_price_change = df.loc[df['Price Change (24-hour %)'].idxmax()]
lowest_price_change = df.loc[df['Price Change (24-hour %)'].idxmin()]

# Save the analysis to a new Excel sheet
with pd.ExcelWriter('Crypto_Analysis.xlsx') as writer:
    df.to_excel(writer, sheet_name='Top 50 Cryptocurrencies', index=False)
    top_5_by_market_cap.to_excel(writer, sheet_name='Top 5 by Market Cap', index=False)
    
    # Create a summary DataFrame
    summary_data = {
        'Average Price of Top 50': [average_price],
        'Highest 24h Change': [f"{highest_price_change['Cryptocurrency Name']} ({highest_price_change['Price Change (24-hour %)']}%)"],
        'Lowest 24h Change': [f"{lowest_price_change['Cryptocurrency Name']} ({lowest_price_change['Price Change (24-hour %)']}%)"]
    }
    summary_df = pd.DataFrame(summary_data)
    
    summary_df.to_excel(writer, sheet_name='Summary', index=False)

print("Analysis completed and saved to 'Crypto_Analysis.xlsx'")
