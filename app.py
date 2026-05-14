import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# Sample Sales Data
# -------------------------------
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Smartwatch'],
    'Sales': [120, 200, 150, 180, 90],
    'Revenue': [600000, 400000, 300000, 90000, 135000]
}

# Create DataFrame
_df = pd.DataFrame(data)

# -------------------------------
# Streamlit App Title
# -------------------------------
st.title("Sales & Revenue Analysis Dashboard")

st.subheader("Sales Data Table")
st.dataframe(_df)

# -------------------------------
# KPI Metrics
# -------------------------------
total_sales = _df['Sales'].sum()
total_revenue = _df['Revenue'].sum()
top_product = _df.loc[_df['Revenue'].idxmax(), 'Product']

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", total_sales)
col2.metric("Total Revenue", f"₹{total_revenue}")
col3.metric("Top Product", top_product)

# -------------------------------
# Sales Chart
# -------------------------------
st.subheader("Product Sales Chart")

fig, ax = plt.subplots()
ax.bar(_df['Product'], _df['Sales'])
ax.set_xlabel("Products")
ax.set_ylabel("Sales")
ax.set_title("Sales by Product")

st.pyplot(fig)

# -------------------------------
# Revenue Chart
# -------------------------------
st.subheader("Revenue Distribution")

fig2, ax2 = plt.subplots()
ax2.pie(_df['Revenue'], labels=_df['Product'], autopct='%1.1f%%')
ax2.set_title("Revenue Share")

st.pyplot(fig2)