
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


# yaha paste

# day 4 : interactive filters

# Region Filter 

regions = ["All"] + sorted(df["region"].unique())
select_region = st.selectbox(
    "Select Region",
    regions
)

# product filter 


products = ["All"] + sorted(df["product"].unique())

selected_product = st.selectbox(
    "Select Product",
    products
)

# payment filter

payments = ["All"] + sorted(df["payment_method"].unique())

selected_payment = st.selectbox(
    "Select Payment",
    payments
)


# ab actual filter 

filtered_df = df.copy()

# region
if select_region != "All":
    filtered_df = filtered_df[
        filtered_df["region"] == select_region
    ]
# Product
if select_region != "All":
    filtered_df = filtered_df[
        filtered_df["product"] == selected_product
    ]
# Payment
if select_region != "All":
    filtered_df = filtered_df[
        filtered_df["payment_method"] == selected_payment
    ]    


total_revenue = np.sum(df["revenue"])    

total_revenue = np.sum(filtered_df["revenue"])
total_orders = len(filtered_df)
average_order = np.mean(filtered_df["revenue"])
highest_order = np.max(filtered_df["revenue"])


# konsa product sabs  jyada revenue lekr aaya hai 

product_sales = (
    filtered_df
    .groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# st.subheader("Product Performance")
# st.bar_chart(product_sales)


# matplotlib ka professional chart
fig, ax = plt.subplots(figsize=(15,5))

ax.bar(
    product_sales.index,
    product_sales.values
)

ax.set_title("Revenue by Product")
# ax.set_xlable("Product")
# ax.set_ylable("Revenue (₹)")
plt.xticks(rotation=30)
st.pyplot(fig)

# sales analysis by region

region_sales = (
    filtered_df
    .groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("🌍 Regional Performance")


fig, ax = plt.subplots(figsize=(15,5))

ax.bar(
    region_sales.index,
    region_sales.values
)
ax.set_title("Revenue by Region")
# ax.set_xlable("Product")
# ax.set_ylable("Revenue (₹)")

st.pyplot(fig)




# Payment analysis

payment_sales = (
    filtered_df
    .groupby("payment_method")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Payment method")
st.bar_chart(payment_sales)

col1 , col2 = st.columns(2)

# left

with col1:
    st.subheader("Product Revenue")

    fig , ax = plt.subplots()

    ax.bar(
        product_sales.index,
        product_sales.values
    )

    plt.xticks(rotation=30)
    st.pyplot(fig)


# right

with col2:

    # Region Pie Chart


    if region_sales.sum() > 0:

        fig,ax = plt.subplots()

        ax.pie(

            region_sales.values,
            labels=region_sales.index,
            autopct="%1.1f%%",
            startangle=90

        )
    else:
        st.warning("No sales available for the selected filter")    

    st.pyplot(fig)

#   Daily revenue calculate

df["date"]  = pd.to_datetime(df["date"])

df["revenue"] = df["quantity"] * df["price"]

daily_sales = (
    df.groupby("date")["revenue"]
    .sum()
    .sort_index()
)
# line chart

fig , ax = plt.subplots()

ax.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o"
)

plt.xticks(rotation=90)

st.pyplot(fig)


# monthly sales

monthly_sales = (
    df.groupby(df["date"].dt.to_period("M"))["revenue"]
    .sum()
)

# print

fig , ax = plt.subplots()

ax.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.xticks(rotation=60)

st.pyplot(fig)

# day3

# Daily revenue
# line chart
# growth
# best sales day

# date range filter

df["date"] = pd.to_datetime(df["date"])

start_date = st.date_input(
    "Start Date",
    df["date"].min().date()
)

end_date = st.date_input(
    "End Date",
    df["date"].max().date()
)






































