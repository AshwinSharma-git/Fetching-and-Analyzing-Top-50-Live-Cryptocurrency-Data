
### **Fetching and Analyzing Top 50 Live Cryptocurrency Data**  

![Crypto](https://upload.wikimedia.org/wikipedia/commons/6/6f/Bitcoin.com_logo.svg)  

## **📌 Project Overview**  
This project fetches live cryptocurrency data using the **CoinGecko API** and analyzes the top 50 cryptocurrencies by market capitalization. It provides real-time insights and updates the data every **5 minutes** in a **live Google Sheet**.  

🔗 **Live Google Sheet:** [Click Here to View](https://docs.google.com/spreadsheets/d/1OYMd20wZhjniF1lf3UKyuw4lvCkv2zMcwW0ZfRUKt-w/edit?usp=sharing)  

---

## **🛠 Features**  
✅ Fetches live **Top 50 Cryptocurrencies** data from CoinGecko API  
✅ Analyzes:  
   - **Top 5 Cryptocurrencies** by Market Cap  
   - **Average Price** of the Top 50  
   - **Biggest Gainer & Loser (24h % Change)**  
✅ **Live Updating Google Sheet** (Every 5 Minutes)  
✅ Stores Data in an Excel Sheet for Further Analysis  

---

## **📂 Project Structure**  
```
📦 Fetching-and-Analyzing-Top-50-Live-Cryptocurrency-Data  
 ┣ 📜 fetch_crypto_data.py         # Fetches live crypto data & stores in Excel  
 ┣ 📜 crypto_analysis.py           # Performs analysis on top 50 cryptocurrencies  
 ┣ 📜 live_crypto_updater.py       # Updates Google Sheet every 5 minutes  
 ┣ 📜 Crypto_Analysis.xlsx         # Analysis results (Excel format)  
 ┣ 📜 Top_50_Cryptocurrencies.xlsx # Raw fetched data (Excel format)  
 ┣ 📜 README.md                    # Project documentation  
```

---

## **🔧 Setup & Installation**  
1️⃣ Clone this repository:  
   ```bash
   git clone https://github.com/AshwinSharma-git/Fetching-and-Analyzing-Top-50-Live-Cryptocurrency-Data.git
   cd Fetching-and-Analyzing-Top-50-Live-Cryptocurrency-Data
   ```  
   
2️⃣ Install dependencies:  
   ```bash
   pip install pandas requests gspread oauth2client schedule
   ```  

3️⃣ Run the scripts:  
   - **Fetch Crypto Data:**  
     ```bash
     python fetch_crypto_data.py
     ```  
   - **Perform Data Analysis:**  
     ```bash
     python crypto_analysis.py
     ```  
   - **Start Live Updater (Google Sheet Refresh Every 5 Minutes):**  
     ```bash
     python live_crypto_updater.py
     ```  

---

## **📊 Live Data Visualization**  
🔹 [View Live Google Sheet](https://docs.google.com/spreadsheets/d/1OYMd20wZhjniF1lf3UKyuw4lvCkv2zMcwW0ZfRUKt-w/edit?usp=sharing)  

---

## **📩 Contact**  
💡 Created by **Ashwin Sharma**  
📧 Email: sharmaashwin880@gmail.com
🔗 GitHub: [AshwinSharma-git](https://github.com/AshwinSharma-git)  

