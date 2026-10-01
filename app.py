import streamlit as st
import streamlit.components.v1 as components

# Đặt layout dạng rộng (wide) để hiển thị 2 ảnh ngang nhau thoải mái
st.set_page_config(
    page_title="Find The Differences Game",
    page_icon="🔍",
    layout="wide"
)

# Ẩn các thanh menu thừa của Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Đặt chiều cao 580px bao trọn trò chơi
components.html(html_code, height=580, scrolling=False)
