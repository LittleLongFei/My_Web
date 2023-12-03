


import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)


st.sidebar.success("The copyright belongs to Shandong University")
st.sidebar.info("Developer: H.Zhang")
st.sidebar.error("Created Time: 2023-5-23")

col1, col2, col3, col4 = st.columns([1,1,1,1.5])

with col3:
    image = Image.open(r'./Resource/4.png')
    st.image(image)

col1, col2, col3, col4 = st.columns([1,1,1.1,1.5])

with col3:
    st.caption('Copyright © 2023, 山东大学 中国·济南')


