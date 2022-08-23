from unicodedata import decimal
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Jiwa 2022',
                    page_icon=':shark:',
                    layout='wide')

### --- LOAD DATAFRAME JIWA
excel_file = 'excel/LAP_KESWA_PKM_PETIR_2022.xlsx'
sheet_name = 'Sasaran 2022 KESWA PKM FIX'
sheet_odgj = 'ODGJ pkm'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='C:R',
                    header=4,
                    nrows=38,
                    decimal='.')

df_odgj = pd.read_excel(excel_file,
                        sheet_name=sheet_odgj,
                        usecols='B:P',
                        header=12,
                        nrows=60,
                        decimal='.')
        


### --- HORIZONTAL BAR
selected = option_menu(
    menu_title=None,
    options=['Sasaran Keswa', 'ODGJ', 'SRQ'],
    default_index=0,
    orientation='horizontal',
)

if selected == 'Sasaran Keswa':
    st.title(f'Laporan {selected}')
    st.subheader('Jumlah Penduduk Proyeksi 2022')

    col1, col2 = st.columns([2, 2])
    ### --- BAR CHARTS TOTAL
    bar_chart = px.bar(df,
                    x='PUSKESMAS',
                    y=['LAKI-LAKI', 'PRP'],
                    barmode='group',
                    template='plotly_white',
                    width=900,
                    height=600,
                    labels={'value':'Total Penduduk'})
    
    col1.plotly_chart(bar_chart)
    
    ### --- SCATTER
    scatter_chart = px.scatter(df,
                                x='LAKI-LAKI',
                                y='PRP',
                                color='PUSKESMAS',
                                trendline='ols',
                                template='seaborn')
    
    col2.plotly_chart(scatter_chart)

    col1, col2 = st.columns([2, 2])

    ### --- BAR CHARTS LAKI-LAKI
    bar_chart = px.bar(df,
                    title='Penduduk Laki-laki Puskesmas Petir',
                    x='PUSKESMAS',
                    y='LAKI-LAKI',
                    color='LAKI-LAKI',
                    color_discrete_sequence=['#568648']*len(df),
                    template='plotly_white',
                    labels={'LAKI-LAKI':'Penduduk Lak-laki'})
    col1.header('Penduduk Pria')
    col1.plotly_chart(bar_chart)

    ### --- BAR CHARTS PEREMPUAN
    bar_chart = px.bar(df,
                    title='Penduduk Perempuan Puskesmas Petir',
                    x='PUSKESMAS',
                    y='PRP',
                    color='PRP',
                    color_discrete_sequence=['#568648']*len(df),
                    template='plotly_white',
                    labels={'PRP':'Penduduk Perempuan'})
    col2.header('Penduduk Wanita')
    col2.plotly_chart(bar_chart)

    
if selected == 'ODGJ':
    st.title(f'Laporan {selected}')
    st.subheader('Pasien Jiwa Petir')
    
if selected == 'SRQ':
    st.title(f'Laporan {selected}')
    st.subheader('Self-Reporting Questionnaire')
    st.write('Petunjuk: Bacalah petunjuk ini seluruhnya sebelum mulai mengisi. Pertanyaan berikut berhubungan dengan masalah yang mungkin mengganggu Anda selama 30 hari terakhir. Apabila Anda menganggap pertanyaan itu berlaku bagi Anda dan Anda mengalami masalah yang disebutkan dalam 30 hari terakhir, berilah tanda pada kolom 1. Sebaliknya, Apabila Anda menganggap pertanyaan itu tidak berlaku bagi Anda dan Anda tidak mengalami masalah yang disebutkan dalam 30 hari terakhir, berilah tanda pada kolom 0. Jika Anda tidak yakin tentang jawabannya, berilah jawaban yang paling sesuai di antara 1 dan 0. Kami tegaskan bahwa, jawaban Anda bersifat rahasia, dan akan digunakan hanya untuk membantu pemecahan masalah Anda.')
    st.write('[SRQ FORM](https://docs.google.com/forms/d/e/1FAIpQLSf9sm-r5j9h1dmd4hNui4-JhfJWzCWTHvcBH75IXnhLyFxS7A/viewform)')

