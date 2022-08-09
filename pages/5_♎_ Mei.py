import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Laporan IGD Januari')

st.header('Mei 2022')
st.subheader('read excel easily with graphic')


### --- LOAD DATAFRAME
excel_file = 'pages/IGD.xlsx'
sheet_name = 'MEI'

df_mei = pd.read_excel(excel_file,
                            sheet_name=sheet_name,
                            usecols='A:CA',
                            header=24,
                            nrows=40)

st.dataframe(df_mei)

### --- BAR CHARTS
bar_chart = px.bar(df_mei,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#354396']*len(df_mei),
                    template='plotly_white')

st.plotly_chart(bar_chart)

### --- PIE CHARTS
pie_chart = px.pie(df_mei,
                    title='Presentasi Penyakit iGD',
                    names='Diagnosa 1')

st.plotly_chart(pie_chart)