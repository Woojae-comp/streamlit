import streamlit as st

st.title("버튼 입력 사용")
clicked = st.button("버튼1")
st.write("버튼1 클릭상태 : ", clicked)

if clicked:
    st.write("버튼 1 클릭 했습니다")
else:
    st.write("버튼 1 실패 했습니다")

st.title("체크 박스 사용")
clicked1 = st.checkbox("체크박스1")
st.write("체크박스 상태", clicked1)

# 라디오 버튼 만들기
st.title("라디오 버튼")
ra_op = ['10','20','30','40']
radio_selected = st.radio('질문 1.5X5+5= ?', ra_op)
st.write("선택한 답 : ", radio_selected)

ra_op2 = ['태권도', '요가', '수영', '음악감상']
radio_selected2 = st.radio('질문 2.좋아하는 운동은?', ra_op2)
st.write("선택한 답 : ", radio_selected2)

# 콤보 박스 만들기
se1_op = ['하이든', '모차르트', '베토벤', '쇼팽']
select2 = st.selectbox("질문 3 : 좋아하는 음악가는?", se1_op)
st.write('선택한 답 :', select2)