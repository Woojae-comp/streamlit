import streamlit as st
from PIL import Image # 이미지 라이브러리

st.title("이미지 표시 방법")

# 컴퓨터 내에 있는 이미지 파일을 열어서 표시
st.subheader("1. 컴퓨터 내의 이미지 파일")
img1 = Image.open(r"data/avenue.jpg")
# 불러와서 뿌려야 함

st.image(img1, width=350, caption = "컴퓨터 내의 이미지 파일을 열어서 표시한 이미지")

st.subheader("2. 웹상의 이미지 파일")
img_url = "https://file.bodnara.co.kr/up/data/112854-1.jpg"
st.image(img_url, width=350, caption = "웹상의 이미지 파일을 열어서 표시한 이미지")