import pandas as pd
import streamlit as st

folder = 'API_ST.INT.ARVL_DS2_en_csv_v2_4902445'
file = 'API_ST.INT.ARVL_DS2_en_csv_v2_4902445.csv'
data = pd.read_csv(f'{folder}/{file}',
                   sep=',', skiprows=3)


top_tourist_countries = data[['Country Name', '2020']].dropna().sort_values('2020', ascending=False).head(20)
top_tourist_countries = top_tourist_countries.reset_index(drop=True)
top_tourist_countries = top_tourist_countries.set_index('Country Name')

st.title('Tourism Stats')
top_tourist_countries
# st.line_chart(x=top_tourist_countries['Country Name'], y=top_tourist_countries['2020'])
st.bar_chart(top_tourist_countries)


