import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Materi',
                    page_icon='🌜',
                    layout='centered')

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

### ----- LOAD ASSETS IMAGE
img_TBC = Image.open('img/TBC_care.png')
img_FIGO = Image.open('img/FIGO_CHART.jpg')
img_UGD = Image.open('img/UGD&IGD.jpg')

### ---- LOAD VIDEO
video_file = open('video/Teknik_Melepas_Helm.mp4', 'rb')
video_bytes = video_file.read()

### ---- MATERI SAMPING
st.sidebar.header('Pilih Materi')
option = st.sidebar.selectbox(label='klik disini',
                                options=['UGD', 'Tuberculosis', 'Rujukan Jiwa', 'Figo Chart'],
                                index=0)
if option == 'UGD':
    st.title(f'Download Materi {option}')

    c1, c2 = st.columns(2)
    with c1:
        st.image(img_UGD)
        st.write('#')
        
    
    with c2:
        st.write('INITIAL ASSESMENT UGD')
        st.write('[Tatalaksana Kegawatdaruratan Trauma](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EWiYLIVu_npPj4yAzuMP6IUB-o-pwDYETu_DBNcmGfdLrQ?e=bVeXLU)')
        st.write('[Terapi Cairan Intravena pd anak](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EbfxL0bG2WtApKt_Wpt0cuYBptZtocEGCcb2aGQqoiWBDg?e=8vTOJJ)')
        st.write('[Tatalaksana Kejang pd anak](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EdeevLlhfY1NpYO6xyOeIpkBbipiL41MUQ2QaNWxyt7fGw?e=o2QphM)')
        st.write('[Tatalaksana Cardiovasacular](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EUNzLpIr6g1Mj6xjyJass34BnuXLEwPBxlz6gHYATPCB8A?e=YafoDZ)')
        st.write('[Kegawatdaruratan Orthopedi](https://pvpmail-my.sharepoint.com/:p:/g/personal/novianil_oficeoriginal_id/EfA_ueOzc8tAjFn-hxuGwVAB21AOCUmjpTVcSdjwKekblw?e=9N56FK)')
    
    ### ---- TOMBOL DOWNLOAD UGD
    with open("download/UGD/UGD.zip", "rb") as file:
     btn = c2.download_button(
             label="Download materi UGD",
             data=file,
             file_name="UGD.zip",
             mime="text/plain"
           )
    
    st.subheader('Teknik Melepas Helm')
    st.video(video_bytes)
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
    
    
    st.subheader('[SEJIWA LOGIN](https://sejiwa.rsjsh.co.id/login)')
    st.write('[Hubungi Whatsapp Layanan Sejiwa](https://api.whatsapp.com/send/?phone=%2B628111533327&text&type=phone_number&app_absent=0)')
    st.write('##')
    st.write(
        '''
            untuk melakukan rujukan pasien jiwa ke RSJ siapkan dokumen :
            - KTP atau Kartu keluarga
            - BPJS
            - FORM dari Puskesmas dalam bentuk PDF kirim ke whatsapp layanan sejiwa
        '''
    )
    ### ---- TOMBOL DOWNLOAD FORM RUJUKAN
    with open("download/Surat rujuk ke rsj (contoh nama).docx", "rb") as file:
     btn = st.download_button(
             label="Download Form Rujukan",
             data=file,
             file_name="Surat rujuk ke rsj (contoh nama).docx",
             mime="text/plain"
           )
if option == 'Figo Chart':
    st.image(img_FIGO)
    ### ----- st.write('[Figo Chart](https://pvpmail-my.sharepoint.com/:b:/g/personal/novianil_oficeoriginal_id/EWrkPIe0DxFPq8K1BDxhHXABg2VCl3M-xlSiw9gJ2bwAJg?e=YrVDNN)')
    ### ---- TOMBOL DOWNLOAD FIGO CHART
    with open("download/figo_chart/FIGO_CHART.pdf", "rb") as file:
     btn = st.download_button(
             label="Download Figo Chart",
             data=file,
             file_name="FIGO_CHART.pdf",
             mime="text/plain"
           )