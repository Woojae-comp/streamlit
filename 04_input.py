import streamlit as st
import datetime

# text 입력
userId = st.text_input('아이디 : ', value='입력하세요', max_chars=15)
userPw = st.text_input('비밀번호 : ', value='abcd', type='password')

if userId == 'streamlit' : 
    if userPw == '1234':
        st.write("로그인 성공")
    else:
        st.write("패스워드 다시 입력하시오")
else:
    st.write("없는 아이디 입니다")

# 날짜 입력

birth = st.date_input("당신의 생일은?", value= datetime.date(1991,10,29))
st.write("당신의 생일", birth)

# 날짜의 범위를 지정
date_range = st.date_input('2. 시작과 끝 날짜를 선택',
                    value=[datetime.date(2021, 4, 10), datetime.date(2023, 5, 17)],
                    min_value=datetime.date(2021, 4, 10),
                    max_value=datetime.date(2023, 5, 17))

st.write("선택한 날짜의 범위 : ", date_range)

# 시간 입력

alarm = st.time_input("알림시간 설정 : ", value= datetime.time(6,00))
st.write("알람설정 시간", alarm)

# 프로토 타입 만들 때, 사용하는 것임