import streamlit as st # pip install streamlit
from streamlit_option_menu import option_menu
import base64

st.set_page_config(page_title='Portofolio', page_icon='🌈', layout='centered', initial_sidebar_state='collapsed')


page_bg_img = f'''
<style>
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


# 1. as a sidebar menu

# 2. horizontal bar
selected = option_menu(
        menu_title=None, #required
        options=['Home', 'Projects', 'Contact', 'Gallery'], #required
        icons=['house', 'book', 'envelope', 'camera'], #optional
        menu_icon='cast', #optional
        default_index=0, #optional
        orientation='horizontal',
        
    )

if selected == "Home":
    st.title(f"{selected}")
    st.subheader('Hi, I am Zico Permadi, MD :wave:')
    st.title('A Data Analyst From Tangerang')
    st.write('I am passionate about finding ways to use Python to be more efficient')
    st.write('[Learn More >>](https://zicoprmd.github.io/)')
if selected == "Projects":
    st.title(f"{selected}")
if selected == "Contact":
    st.title(f"{selected}")
    st.header(':mailbox: Get In Touch With Me!')

    contact_form = '''
    <form method="POST" action="https://formsubmit.co/zicoprmd@gmail.com" enctype="multipart/form-data">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <input type="file" name="attachment" accept="image/png, image/jpeg">
        <button type="submit">Send</button>
    </form>
    '''

    st.markdown(contact_form, unsafe_allow_html=True)

# use local css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')