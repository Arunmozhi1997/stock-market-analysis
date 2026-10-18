import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os


# DB Connection

  
engine = create_engine(os.getenv("DATABASE_URL"))

@st.cache_data
def load_table(table):
    return pd.read_sql_table(table, engine)

# Load all tables


prices    = load_table("stock_prices")
year_ret  = load_table("yearly_returns")
greens    = load_table("top10_green")
reds      = load_table("top10_red")
vol_df    = load_table("volatility")
cum       = load_table("cumulative_returns")
corr      = load_table("correlation_matrix")



# Convert date format
prices["date"] = pd.to_datetime(prices["date"])
cum["date"] = pd.to_datetime(cum["date"])

# Streamlit Page Setup


st.title(" Stock Market SQL Dashboard")

# Sidebar Filters

tickers = sorted(prices["Ticker"].unique())
stock = st.sidebar.selectbox("Select Stock", tickers)

date_min = prices["date"].min()
date_max = prices["date"].max()

date_range = st.sidebar.date_input("Select Date Range",
    [date_min, date_max]
)
st.write("Selected Stock:", stock)
col1, col2, col3 = st.columns(3)
close_df = prices[prices["Ticker"] == stock]
close_df = close_df[(close_df["date"] >= pd.to_datetime(date_range[0])) &
                    (close_df["date"] <= pd.to_datetime(date_range[1]))]

latest_price = close_df["close"].iloc[-1]
yearly_val = year_ret[year_ret["Ticker"] == stock]["Yearly_Return"].values[0]
vola_val = vol_df[vol_df["Ticker"] == stock]["Volatility"].values[0]

col1.metric("Latest Price", round(latest_price,2))
col2.metric("Yearly Return", f"{round(yearly_val*100,2)} %")
col3.metric("Volatility", round(vola_val,4))

# Line Chart

st.subheader(" Stock Price Trend")

chart_df = close_df.sort_values("date")
fig = px.line(chart_df, x="date", y="close", title=f"{stock} Closing Price")
st.plotly_chart(fig, use_container_width=True)

# Cumulative Return Chart


st.subheader("Cumulative Return Trend")

cum_stock = cum[cum["Ticker"] == stock]
fig2 = px.line(cum_stock, x="date", y="Cumulative_Return", title=f"{stock} return trend")
st.plotly_chart(fig2, use_container_width=True)


# Top Gainers & Losers


st.subheader(" Top 10 Best Performing Stocks")
st.dataframe(greens)

st.subheader(" Top 10 Worst Performing Stocks")
st.dataframe(reds)



# Correlation Heatmap


st.subheader(" Stock Correlation Matrix")

st.dataframe(corr)
