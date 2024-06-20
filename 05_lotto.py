import random
import streamlit as st
import datetime

def generator():
    lotto=[]
    while len(lotto) < 6:
        number = random.randint(1,45)
        if number not in lotto:
            lotto.append(number)
    lotto.sort()
    return lotto

st.title("로또 생성기")

btn = st.button("generator")

if btn:
    for i, num in enumerate(generator(), start=1):
        st.subheader(f"{i}번째 숫자 : {num}")

if btn:
    for i in range(1,6):
        st.subheader(f"{i}번째 로또번호 : {generator()}")
    st.write(f"생성된 시간 : , {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
