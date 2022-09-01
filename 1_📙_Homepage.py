import pandas as pd
import streamlit as st
import plotly.express as px
import base64

st.set_page_config(page_title='Laporan IGD', page_icon='⛈️', layout='centered', initial_sidebar_state='collapsed')


page_bg_img = f'''
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
[data-testid="stAppViewContainer"] {{
background-image: url('https://images.unsplash.com/photo-1660756010411-be7aed1b88cb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2050&q=80');
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

st.title('IGD ⚡')
st.sidebar.header('Main Page')
st.sidebar.success('Scroll sidebar disini!')



### --- LOAD DATAFRAME
excel_file = 'excel/IGD2022.xlsx'
sheet_name = '2022'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='A:D',
                    nrows=13)

### --- BAR CHARTS
bar_chart = px.bar(df,
                    title='IGD 2022',
                    x='Bulan',
                    y=['BPJS', 'Umum'],
                    template='seaborn',
                    labels={'value':'Total'})

st.plotly_chart(bar_chart)

