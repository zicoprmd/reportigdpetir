import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Laporan Pelayanan Lansia 2022', layout='centered')

page_bg_img = f'''
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
[data-testid="stAppViewContainer"] {{
background-size: cover;
}}

[data-testid='stHeader'] {{
    background-color: rgba(0, 0, 0, 0);
}}

[data-testid='stToolbar'] {{
right: 2rem;
}}

</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

### --- LOAD DATAFRAME JIWA
excel_file = 'excel/LANSIA2022.xlsx'
sheet_name = 'LANSIA2022'

df = pd.read_excel(excel_file, sheet_name=sheet_name,
                    usecols='A:D', nrows=15)

### BAR CHART

bar_chart = px.bar(df, title='Lansia 2022',
                    x='Bulan',
                    y=['Pra Lansia', 'Lansia', 'Lansia Risti'],
                    template='seaborn')

st.plotly_chart(bar_chart)