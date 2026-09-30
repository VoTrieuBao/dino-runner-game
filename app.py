import streamlit as st
import streamlit.components.v1 as components

# Cấu hình giao diện Streamlit
st.set_page_config(
    page_title="T-Rex Dinosaur Game",
    page_icon="🦖",
    layout="centered"
)

# Ẩn bớt thanh menu mặc định của Streamlit để giao diện gọn gàng
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Đọc nội dung file index.html
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    # Nhúng game vào Streamlit qua thẻ iframe
    components.html(html_code, height=520, scrolling=False)
except FileNotFoundError:
    st.error("Không tìm thấy file index.html! Hãy đảm bảo file index.html nằm cùng thư mục với app.py.")