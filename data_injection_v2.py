import yfinance as yf
import mysql.connector
from mysql.connector import Error

# MySQL connection
try:
    connection = mysql.connector.connect(user='username', 
                                         password='password',
                                         host='localhost',
                                         database='finance_nifty50')
    if connection.is_connected():
        print("Successfully connected to MySQL")
except Error as e:
    print("Error while connecting to MySQL", e)

cursor = connection.cursor()

# List of companies
companies = [
    ("ADANIENT.NS", "Adani Enterprises Ltd."),
    ("ADANIPORTS.NS", "Adani Ports and Special Economic Zone Ltd."),
    ("APOLLOHOSP.NS", "Apollo Hospitals Enterprise Ltd."),
    ("ASIANPAINT.NS", "Asian Paints Ltd."),
    ("AXISBANK.NS", "Axis Bank Ltd."),
    ("BAJAJ-AUTO.NS", "Bajaj Auto Ltd."),
    ("BAJFINANCE.NS", "Bajaj Finance Ltd."),
    ("BAJAJFINSV.NS", "Bajaj Finserv Ltd."),
    ("BPCL.NS", "Bharat Petroleum Corporation Ltd."),
    ("BHARTIARTL.NS", "Bharti Airtel Ltd."),
    ("BRITANNIA.NS", "Britannia Industries Ltd."),
    ("CIPLA.NS", "Cipla Ltd."),
    ("COALINDIA.NS", "Coal India Ltd."),
    ("DIVISLAB.NS", "Divi''s Laboratories Ltd."),
    ("DRREDDY.NS", "Dr. Reddy''s Laboratories Ltd."),
    ("DUMMYREL.NS", "Dummy - Jio Financial Services Ltd."),
    ("EICHERMOT.NS", "Eicher Motors Ltd."),
    ("GRASIM.NS", "Grasim Industries Ltd."),
    ("HCLTECH.NS", "HCL Technologies Ltd."),
    ("HDFCBANK.NS", "HDFC Bank Ltd."),
    ("HDFCLIFE.NS", "HDFC Life Insurance Company Ltd."),
    ("HEROMOTOCO.NS", "Hero MotoCorp Ltd."),
    ("HINDALCO.NS", "Hindalco Industries Ltd."),
    ("HINDUNILVR.NS", "Hindustan Unilever Ltd."),
    ("ICICIBANK.NS", "ICICI Bank Ltd."),
    ("ITC.NS", "ITC Ltd."),
    ("INDUSINDBK.NS", "IndusInd Bank Ltd."),
    ("INFY.NS", "Infosys Ltd."),
    ("JSWSTEEL.NS", "JSW Steel Ltd."),
    ("KOTAKBANK.NS", "Kotak Mahindra Bank Ltd."),
    ("LTIM.NS", "LTIMindtree Ltd."),
    ("LT.NS", "Larsen & Toubro Ltd."),
    ("M&M.NS", "Mahindra & Mahindra Ltd."),
    ("MARUTI.NS", "Maruti Suzuki India Ltd."),
    ("NTPC.NS", "NTPC Ltd."),
    ("NESTLEIND.NS", "Nestle India Ltd."),
    ("ONGC.NS", "Oil & Natural Gas Corporation Ltd."),
    ("POWERGRID.NS", "Power Grid Corporation of India Ltd."),
    ("RELIANCE.NS", "Reliance Industries Ltd."),
    ("SBILIFE.NS", "SBI Life Insurance Company Ltd."),
    ("SBIN.NS", "State Bank of India"),
    ("SUNPHARMA.NS", "Sun Pharmaceutical Industries Ltd."),
    ("TCS.NS", "Tata Consultancy Services Ltd."),
    ("TATACONSUM.NS", "Tata Consumer Products Ltd."),
    ("TATAMOTORS.NS", "Tata Motors Ltd."),
    ("TATASTEEL.NS", "Tata Steel Ltd."),
    ("TECHM.NS", "Tech Mahindra Ltd."),
    ("TITAN.NS", "Titan Company Ltd."),
    ("UPL.NS", "UPL Ltd."),
    ("ULTRACEMCO.NS", "UltraTech Cement Ltd."),
    ("WIPRO.NS", "Wipro Ltd.")
]

# Inserting companies into Companies table
for company in companies:
    # Escape single quotes in the company name
    company_name = company[1].replace("'", "''")
    insert_query = f"""INSERT INTO Companies (CompanyID, Name, Symbol) 
                       VALUES ('{company[0]}', '{company_name}', '{company[0]}');"""
    cursor.execute(insert_query)

# Fetching stock price data and inserting into StockPrices table
for company in companies:
    data = yf.download(company[0], start='2022-01-01', end='2023-01-01')
    for index, row in data.iterrows():
        insert_query = f"""INSERT INTO StockPrices (Date, Open, High, Low, Close, Adj_Close, Volume, Symbol) 
                           VALUES ('{index.strftime('%Y-%m-%d')}', {row['Open']}, {row['High']}, {row['Low']}, {row['Close']}, {row['Adj Close']}, {row['Volume']}, '{company[0]}');"""
        cursor.execute(insert_query)

# Committing the transaction and closing the connection
connection.commit()
cursor.close()
connection.close()
