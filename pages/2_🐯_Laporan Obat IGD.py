import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Laporan Obat IGD',
                    page_icon='🐯',
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
img_GFORM = Image.open('img/gformicons.png')

st.title(f'Laporan Inputan Obat UGD')
    
image_col, text_col = st.columns([2,2])
with image_col:
    st.image(img_GFORM)
with text_col:
    st.write('#')
    st.subheader('[PEMAKAIAN OBAT UGD](https://docs.google.com/forms/d/e/1FAIpQLSfflHsXsmv8wjUubQN57dCA6jaxoy27XcF8_czspj_VjkKSJQ/viewform)')
    st.subheader('[PEMAKAIAN ALKES UGD](https://docs.google.com/forms/d/e/1FAIpQLSdBztVcpjaFhS8u89UuI41NDbctz59uDM-AhOeFUDZrQXJz6w/viewform)')
    

### ---- TOMBOL DOWNLOAD ISTC
# with open("download/tuberculosis/ISTC.zip", "rb") as file:
#     btn = st.download_button(
#             label="Download materi ISTC",
#             data=file,
#             file_name="ISTC.zip",
#             mime="text/plain"
#            )