


import streamlit as st

from PIL import Image

# page Configuration

st.set_page_config(
    page_title="Hui-Zhang",
    page_icon="🏡",
    layout="wide",
)


# 头像
image = Image.open(r'./Resource/1.png')
st.image(image, width=500, height=300)



col1, col2, col3, col4 = st.columns([1,1,1,1.5])

with col3:
    image = Image.open(r'./Resource/4.png')
    st.image(image)

col1, col2, col3, col4 = st.columns([1,1,1.1,1.5])

with col3:
    st.caption('Copyright @ 2023, 山东大学 中国·济南')


