import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='IGD 2022',
                    page_icon=':apple:',
                    layout='wide')

### --- LOAD DATAFRAM JIWA
excel_file = 'excel/LAP_KESWA_PKM_PETIR_2022.xlsx'
sheet_name = 'Sasaran 2022 KESWA PKM FIX'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    usecols='C:R',
                    header=4,
                    nrows=38,
                    decimal='.')

#st.dataframe(df)
        

### --- HORIZONTAL BAR
selected = option_menu(
    menu_title=None,
    options=['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus'],
    default_index=0,
    menu_icon='menu-up',
    orientation='horizontal',
)

if selected == 'Sasaran Keswa':
    st.title(f'Laporan {selected}')
    st.subheader('Jumlah Penduduk Proyeksi 2022')

    ### --- BAR CHARTS TOTAL
    bar_chart = px.bar(df,
                    x='PUSKESMAS',
                    y=['LAKI-LAKI', 'PRP'],
                    barmode='group',
                    template='plotly_white',
                    width=1000,
                    height=600,
                    labels={'value':'Total Penduduk'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS LAKI-LAKI
    bar_chart = px.bar(df,
                    title='Penduduk Laki-laki Puskesmas Petir',
                    x='PUSKESMAS',
                    y='LAKI-LAKI',
                    color='LAKI-LAKI',
                    color_discrete_sequence=['#568648']*len(df),
                    template='plotly_white',
                    width=1000,
                    height=600,
                    labels={'LAKI-LAKI':'Penduduk Lak-laki'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS PEREMPUAN
    bar_chart = px.bar(df,
                    title='Penduduk Perempuan Puskesmas Petir',
                    x='PUSKESMAS',
                    y='PRP',
                    color='PRP',
                    color_discrete_sequence=['#568648']*len(df),
                    template='plotly_white',
                    width=1000,
                    height=600,
                    labels={'PRP':'Penduduk Perempuan'})

    st.plotly_chart(bar_chart)

if selected == 'ODGJ':
    st.title(f'Laporan {selected}')

if selected == 'SRQ':
    st.title(f'Laporan {selected}')
