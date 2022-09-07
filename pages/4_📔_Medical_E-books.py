from ssl import Options
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Medical E-books',
                    page_icon=':books:',
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

### ---- MATERI SAMPING

option = st.sidebar.selectbox(label='Choose E-books',
                                options=['Anatomy & Physiology', 'Medical MicroBiology', 'Interna'],
                                index=0)

if option == 'Anatomy & Physiology':
    st.title(f'{option}')
    st.write('[PRINCIPLES OF ANATOMY AND PHYSIOLOGY - Tortora - 14th Ed](https://pvpmail-my.sharepoint.com/:b:/g/personal/novianil_oficeoriginal_id/Ea3X3IbqM1RHviqnC6m85ewBLamkN65-QlYlCdf-_8gsVg?e=PTFuhg)')

if option == 'Medical MicroBiology':
    st.title(f'{option}')
    st.write('[The BIg Pictures Medical Mircobiology](https://pvpmail-my.sharepoint.com/:b:/g/personal/novianil_oficeoriginal_id/EQJs8DfL79lNqJ10uXFIGHkBVH2gXnOtxlCh51KyFStiQw?e=pafhhD)')

if option == 'Interna':
    st.title(f'{option}')
    st.write('[Ilmu Penyakit Dalam Edisi IV](https://pvpmail-my.sharepoint.com/:b:/g/personal/novianil_oficeoriginal_id/EUGnqNa8HfxAg6yKIx4JvC8BeqM2yJldPR2FexN7SC6G7w?e=ELgyTc)')