import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.JPG', width=400)

with col2:
    st.title('Ali Sina Sultani')
    content = ''''
        Hi,I'm Ali Sina sultani, I'm softwear Engineer, and python programmer
    '''
    st.info(content)
