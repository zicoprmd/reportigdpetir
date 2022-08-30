import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Materi',
                    layout='centered')

### ----- LOAD ASSETS IMAGE
img_TBC = Image.open('img/TBC_care.png')
img_FIGO = Image.open('img/FIGO_CHART.jpg')

### ---- MATERI SAMPING
st.sidebar.header('Pilih Materi')
option = st.sidebar.selectbox(label='klik disini',
                                options=['Tuberculosis', 'Rujukan Jiwa', 'FIGO CHART'],
                                index=0)

if option == 'Tuberculosis':
    st.title(f'Download Materi {option}')
    
    image_col, text_col = st.columns([2,2])
    with image_col:
        st.image(img_TBC)
    with text_col:
        st.write('#')
        st.subheader('[ISTC Diagnosis 2022](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EensITD4snZGu-13zlkf0VoBY9IDBjXp7EhRq0-A_MghVQ)')
        st.subheader('[ISTC Terapi 2022](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EWbMBpYk281JoQCrHKGwn6QBhCYRIZhHBThBQzZ5XvYygw)')
        st.subheader('[ISTC Kondisi Khusus 2022](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/ETzP0cIxDJRIv22WV93Sy8YBTgb8E7YZzslvFaVM03Uudg)')
        st.subheader('[ISTC IKA TPT 2022](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EW4PQ_kqKldCnPJYI1RxKrABDF79JnasjDUmIsP7fNsYNw)')

    ### ---- TOMBOL DOWNLOAD ISTC
    with open("download/tuberculosis/ISTC.zip", "rb") as file:
     btn = st.download_button(
             label="Download materi ISTC",
             data=file,
             file_name="ISTC.zip",
             mime="text/plain"
           )
if option == 'Rujukan Jiwa':
    st.title(f'Download Form {option}')
    ### ---- TOMBOL DOWNLOAD FORM RUJUKAN
    with open("download/Surat rujuk ke rsj (contoh nama).docx", "rb") as file:
     btn = st.download_button(
             label="Download Form Rujukan",
             data=file,
             file_name="Surat rujuk ke rsj (contoh nama).docx",
             mime="text/plain"
           )
    
    st.write('[Hubungi Whatsapp Layanan Sejiwa](https://api.whatsapp.com/send/?phone=%2B628111533327&text&type=phone_number&app_absent=0)')

if option == 'FIGO CHART':
    st.image(img_FIGO)
    st.write('[FIGO CHART](https://brtyl-my.sharepoint.com/:b:/g/personal/zicoprmd_apps365_work/EfNZmV25gp1Kopr6UCPRFqsB0vl3Hc_eGPV22PgrKk_C5Q?e=rW0gug)')
    ### ---- TOMBOL DOWNLOAD FIGO CHART
    with open("download/figo_chart/FIGO_CHART.pdf", "rb") as file:
     btn = st.download_button(
             label="Download Figo Chart",
             data=file,
             file_name="FIGO_CHART.pdf",
             mime="text/plain"
           )