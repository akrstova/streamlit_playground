import streamlit as st
import pandas as pd

st.title("Status dashboard")


@st.cache_data
def read_status_data():
    return pd.read_csv("data/statuses.csv", sep=";")


col1, col2 = st.columns(2)

data = read_status_data()

with col1:
    st.write(data)

with col2:
    st.expander("First half of data").write(data[: len(data) // 2])
    st.expander("Second half of data").write(data[len(data) // 2 :])
