import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="POST PANDEMIC EFFECTS OF COVID-19", layout="wide"
                  )

df = pd.read_csv(
    io = 'owid-covid-data.csv',
    engine = 'openpyxl',
    sheet_name = 'owid-covid-data',
    skiprows = 3,
    usecols = 'A:BK',
    nrows = 160000,
)

print(df.head())