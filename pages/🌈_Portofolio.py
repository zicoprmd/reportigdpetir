from turtle import title
import streamlit as st
from streamlit_option_menu import option_menu

# 1. as a sidebar menu

# 2. horizontal bar

selected = option_menu(
        menu_title='Main menu', #required
        options=['Home', 'Projects', 'Contact'], #required
        icons=['house', 'book', 'envelope'], #optional
        menu_icon='cast', #optional
        default_index=0, #optional
        orientation='horizontal',
    )

if selected == "Home":
    st.title(f"{selected}")
    st.subheader('Hi, I am Zico Permadi, MD :wave:')
    st.title('A Data Analyst From Tangerang')
    st.write('I am passionate about finding ways to use Python to be more efficient')
    st.write('[Learn More >](https://zicoprmd.github.io/)')
if selected == "Projects":
    st.title(f"{selected}")
if selected == "Contact":
    st.title(f"{selected}")
