import streamlit as st

from streamlit_extras.bottom_container import bottom

st.set_page_config('UltraLM',layout='wide')

header_section=st.container()
chat_section=st.container()

with chat_section:
    with st.chat_message('ai'):
        st.write('hello')





# This will remain fixed to the buttom
with bottom():
    chat_input_col,upload_col=st.columns([0.7,0.3])

    with chat_input_col:
        input=st.chat_input('What do you want to research?')
    
    with upload_col.popover('Uplaod Knowledge', use_container_width=True):
        files=st.file_uploader('Enter Files to be uploaded to knowledge base',accept_multiple_files=True)
        if st.button('Upload'):
            st.write('Dummy Upload')



