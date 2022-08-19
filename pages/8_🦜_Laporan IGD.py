from cProfile import label
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title='IGD 2022',
                    page_icon=':hospital:',
                    layout='wide')

### --- LOAD DATAFRAME JANUARI
excel_file = 'excel/IGD.xlsx'
sheet_name = 'JANUARI'

df_januari = pd.read_excel(excel_file,
                            sheet_name=sheet_name,
                            usecols='A:CA',
                            header=24,
                            nrows=29,
                            decimal='.')

### --- LOAD DATAFRAME FEBRUARI

sheet_name1 = 'FEBRUARI'

df_februari = pd.read_excel(excel_file,
                            sheet_name=sheet_name1,
                            usecols='A:CA',
                            header=24,
                            nrows=31)

### --- LOAD DATAFRAME MARET

sheet_name2 = 'MARET'

df_maret = pd.read_excel(excel_file,
                            sheet_name=sheet_name2,
                            usecols='A:CA',
                            header=24,
                            nrows=33)

### --- LOAD DATAFRAME APRIL

sheet_name3 = 'APRIL'

df_april = pd.read_excel(excel_file,
                            sheet_name=sheet_name3,
                            usecols='A:CA',
                            header=24,
                            nrows=40)

### --- LOAD DATAFRAME MEI

sheet_name4 = 'MEI'

df_mei = pd.read_excel(excel_file,
                            sheet_name=sheet_name4,
                            usecols='A:CA',
                            header=24,
                            nrows=40)

### --- LOAD DATAFRAME JUNI

sheet_name5 = 'JUNI'

df_juni = pd.read_excel(excel_file,
                            sheet_name=sheet_name5,
                            usecols='A:CA',
                            header=24,
                            nrows=50)

### --- LOAD DATAFRAME JULI

sheet_name6 = 'JULI'

df_juli = pd.read_excel(excel_file,
                            sheet_name=sheet_name6,
                            usecols='A:CA',
                            header=24,
                            nrows=60)
###################### END DATAFRAME


### --- stremlit option menu
### --- HORIZONTAL BAR
selected = option_menu(
    menu_title=None,
    options=['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'],
    icons=['1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle', '1-circle'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
)

if selected == 'Januari':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_januari,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence=['#35CC96']*len(df_januari),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_januari,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Februari':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_februari,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#65C096']*len(df_februari),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_februari,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Maret':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_maret,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#655796']*len(df_maret),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_maret,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'April':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_april,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#F5C786']*len(df_april),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_april,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Mei':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_mei,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#354396']*len(df_mei),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_mei,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Juni':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_juni,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#559896']*len(df_juni),
                    template='plotly_white',
                    width=1200,
                    height=700,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_juni,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Juli':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')

    ### --- BAR CHARTS
    bar_chart = px.bar(df_juli,
                    title='Grafik Penyakit IGD',
                    x='Diagnosa 1',
                    color_discrete_sequence= ['#355F22']*len(df_juli),
                    template='plotly_white',
                    width=1200,
                    height=1000,
                    labels={'count':'Jumlah', 'Diagnosa 1':'Nama Penyakit'})

    st.plotly_chart(bar_chart)

    ### --- BAR CHARTS KELURAHAN
    bar_kelurahan1 = px.bar(df_juli,
                    title='Grafik Asuransi terhadap Tempat Tinggal Pasien',
                    x='Asuransi',
                    barmode='group',
                    color='Kelurahan',
                    template='plotly_white',
                    width=1000,
                    height=500,
                    labels={'count':'Jumlah'})

    st.plotly_chart(bar_kelurahan1)

if selected == 'Agustus':
    st.title(f'Laporan IGD {selected}')
    st.subheader(f'{selected} 2022')
    