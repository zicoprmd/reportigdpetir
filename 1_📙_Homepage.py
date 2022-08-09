import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Laporan IGD', page_icon='⛈️')

st.title('IGD ⚡ mainpage')
st.sidebar.success('Scroll sidebar disini!')


### --- LOAD DATAFRAME
excel_file = 'IGD2022.xlsx'
sheet_name = '2022'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:B',
                    nrows=13)

### --- BAR CHARTS
bar_chart = px.bar(df,
                    title='IGD 2022',
                    x='Bulan',
                    y='Total',
                    color_discrete_sequence=['#C492A1']*len(df),
                    template='plotly_white')

st.plotly_chart(bar_chart)