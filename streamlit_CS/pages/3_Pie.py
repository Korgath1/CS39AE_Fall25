import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Interactive Pie Chart")

# ---------- Check CSV file ----------
csv_path = "data/pie_demo.csv"
st.write("Looking for CSV at:", os.path.abspath(csv_path))

if not os.path.exists(csv_path):
    st.error("CSV file not found! Please make sure 'data/pie_demo.csv' exists.")
    st.stop()

# ---------- Load CSV ----------
data = pd.read_csv(csv_path)

# Show a preview of the data
st.subheader("Data Preview")
st.dataframe(data)

# ---------- Pie Chart ----------
st.subheader("Pie Chart Visualization")

# Let user pick title and columns
chart_title = st.text_input("Enter a title for the pie chart:", "My Sample Pie Chart")
category_col = st.selectbox("Choose category column:", data.columns, index=0)
value_col = st.selectbox("Choose value column:", data.columns, index=1)

# Create interactive pie chart
fig = px.pie(data, names=category_col, values=value_col, title=chart_title)
st.plotly_chart(fig, use_container_width=True)