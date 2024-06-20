import streamlit as st
from PIL import Image
import pandas as pd

st.header("사용자 지정 화면 분할")

# 세로 단 분할
df2 = pd.read_csv("data\공장별_생산현황2.csv", index_col='year')

[col1, col2] = st.columns(2)
# 분할 할 시, 반드시 메소드에 숫자 넣어주고, 받는 변수는 리스트로 받아야함

with col1:
    st.subheader("DataFrame")
    st.dataframe(df2)

with col2:
    st.subheader("Chart")
    st.line_chart(df2)

# 너비 다르게 해줄 때
columns = st.columns([1.2, 1.0, 0.8])

image_files = ['dog.png', 'cat.png', 'bird.png']
capts = ['강아지', '고양이', '새']

for k in range(len(columns)):
    with columns[k]:
        st.subheader(capts[k])
        img_call = Image.open("D:/workspace_cwj/visual/data/"+image_files[k])
        st.image(img_call, caption=capts[k])