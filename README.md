📈 Stock Market Performance Analysis

Analyses daily stock prices for a set of listed companies to find the best and worst performers, the most volatile stocks and how stocks move together, with results stored in PostgreSQL and shown in a Streamlit dashboard and a Power BI report.

Show Image Show Image Show Image Show Image

📊 What it calculates
Daily and cumulative returns for each stock
Yearly returns, with the top 10 gainers and top 10 losers
Volatility (standard deviation of daily returns)
A correlation matrix of closing prices
🖥️ Dashboard
Price trend for any stock over a chosen date range
Cumulative return trend
Top 10 best and worst performing stocks
Stock correlation heatmap
📁 Project structure
File	Purpose
data_stock.ipynb	Combines the raw stock files into one dataset
stock_sql.ipynb	Computes the metrics and writes them to PostgreSQL
stock_analysis.py	Streamlit dashboard
stock_analysisbi.pbix	Power BI report
⚙️ Run it locally
bash
pip install -r requirements.txt
$env:DATABASE_URL="postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/stockdb"
# Run data_stock.ipynb, then stock_sql.ipynb
streamlit run stock_analysis.py
👤 Author

Arunmozhi M · Portfolio · LinkedIn
