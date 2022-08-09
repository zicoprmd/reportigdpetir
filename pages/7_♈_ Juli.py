import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Laporan IGD Juli')

st.header('Juli 2022')
st.subheader('read excel easily with graphic')


### --- LOAD DATAFRAME
excel_file = 'pages/IGD.xlsx'
sheet_name = 'JULI'

df_juli = pd.read_excel(excel_file,
                            sheet_name=sheet_name,
                            usecols='A:CA',
                            header=24,
                            nrows=60)

st.dataframe(df_juli)

### --- BAR CHARTS
bar_chart = px.bar(df_juli,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#35CC22']*len(df_juli),
                    template='plotly_white')

st.plotly_chart(bar_chart)

### --- PIE CHARTS
pie_chart = px.pie(df_juli,
                    title='Presentasi Penyakit iGD',
                    names='Diagnosa 1')

st.plotly_chart(pie_chart)