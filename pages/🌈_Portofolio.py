import streamlit as st # pip install streamlit
from streamlit_option_menu import option_menu
import requests

from streamlit_lottie import st_lottie


st.set_page_config(page_title='Portofolio', page_icon='🌈', layout='centered', initial_sidebar_state='collapsed')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

### ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_4kx2q32n.json")

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


# 1. as a sidebar menu

# 2. horizontal bar
selected = option_menu(
        menu_title=None, #required
        options=['Home', 'Projects', 'Contact', 'Gallery', 'My File'], #required
        icons=['house', 'book', 'envelope', 'camera'], #optional
        menu_icon='cast', #optional
        default_index=0, #optional
        orientation='horizontal',        
    )

if selected == "Home":
    st.title(f"{selected}")
    with st.container():
        st.subheader('Hi, I am Zico Permadi, MD :wave:')
        st.title('A Data Analyst From Tangerang')
        st.write('I am passionate about finding ways to use Python to be more efficient and effective')
        st.write('[Learn More >>](https://zicoprmd.github.io/)')
        ### --- WHAT I DO ---
    with st.container():
        left_col, right_col = st.columns([2,1])
        with left_col:
            st.header('What I do')
            st.write('##')
            st.write(
                '''
                On my Youtube channel I am creating tutorials for people who:
                - are looking for a way to leverage the power of Python in their day-to-day work.
                - are struggling with repetitive tasks in Excel and are looing for a way to use Python.
                - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                - are working with Excel and founf themselves thinking - "there has to be a better way."
                
                If this sounds interesting to you, consider subscribing and turning on the notifications, so you don't miss any content.
                '''
            )
            st.write()
        with right_col:
            st.write('##')
            st.write('##')
            st.write('##')
            st_lottie(lottie_coding, height=300, key='coding')
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

if selected == "My File":
    st.write('[ACLS dr zico permadi](https://pvpmail-my.sharepoint.com/:b:/g/personal/novianil_oficeoriginal_id/EdvCTPrB9blNgiFgJr0IOdwB5wGhX13JkdRcbarLQsBseg?e=1IU4d8)')