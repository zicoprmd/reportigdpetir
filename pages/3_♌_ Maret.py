import pandas as pd
import streamlit as st
import plotly.express as px
import base64

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64('./img/image2.jpg')

page_bg_img = f'''
<style>


[data-testid='stToolbar'] {{
right: 2rem;
}}

[data-testid='stSidebar'] > div:first-child {{
    background-image: url('data:image/png;base64,{img}');
    background-size: cover;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Laporan IGD Februari')

st.header('Maret 2022')
st.subheader('read excel easily with graphic')


### --- LOAD DATAFRAME
excel_file = 'pages/IGD.xlsx'
sheet_name = 'MARET'

df_maret = pd.read_excel(excel_file,
                            sheet_name=sheet_name,
                            usecols='A:CA',
                            header=24,
                            nrows=33)

st.dataframe(df_maret)

### --- BAR CHARTS
bar_chart = px.bar(df_maret,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#65C796']*len(df_maret),
                    template='plotly_white')

st.plotly_chart(bar_chart)

### --- PIE CHARTS
pie_chart = px.pie(df_maret,
                    title='Presentasi Penyakit IGD',
                    names='Diagnosa 1')

st.plotly_chart(pie_chart)