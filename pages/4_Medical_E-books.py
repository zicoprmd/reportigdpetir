from ssl import Options
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Medical E-books',
                    page_icon=':books:',
                    layout='centered')

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