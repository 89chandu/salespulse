
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SalesPulse",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SalesPulse")
st.subheader("Business Analytics Dashboard")

df = pd.read_csv("data/sales.csv")

df["revenue"] = df["quantity"] * df["price"]

st.write(df)

total_revenue = np.sum(df["revenue"])

total_orders = len(df)

average_order = np.mean(df["revenue"])

highest_order = np.max(df["revenue"])

col1 , col2 , col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col2.metric(
    "🧾 Total Orders",
    total_orders
)

col3.metric(
    "📝 Average Order",
    f"₹{average_order:,.0f}"
)

col4.metric(
    "🚀 Highest Order",
    f"₹{highest_order:,.0f}"
)


# konsa product sabs  jyada revenue lekr aaya hai 

product_sales = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Product Performance")
st.bar_chart(product_sales)


# matplotlib ka professional chart








