import streamlit as st
from PIL import Image

# 사이드바 구성

st.sidebar.title("사이드바")
st.sidebar.header("텍스트 입력")
userId = st.sidebar.text_input("ID", value="streamlit", max_chars=15)
userPw = st.sidebar.text_input("ID", value="abcd", type="password")


st.sidebar.header("셀렉트 박스")
sel_opt=['진주기 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정연']
user_opt = st.sidebar.selectbox("좋아하는 작품은?", sel_opt)
st.sidebar.write("선택한 작품 : ", user_opt)

st.title("스트림릿 메인 화면")
# folder = "D:\workspace_cwj\visual\data\"
image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png']

sel_img_index = sel_opt.index(user_opt)
# 선택한 항목의 맞는 이미지 파일이 무엇인지 지정

image_file = image_files[sel_img_index]
img_local = Image.open(r'D:/workspace_cwj/visual\data/'+image_file)
st.image(img_local, caption=user_opt)