import streamlit
import pandas as pd
import matplotlib as plt
from matplotlib import font_manager, rc

plt.rc('font', family="Malgun Gothic")

# 텍스트 요소
streamlit.title("인공지능 모델배포")
streamlit.header("헤더")
streamlit.text("차우재, 일반텍스트 파일 입니다.")
streamlit.markdown("마크다운")

# 데이터 요소
df = pd.read_csv("data/korea_rain1.csv")

# 인식이 잘 안될 경우
# 1. pd.read_csv(r"data/korea_rain1.csv")
# 2. 절대경로 - 경로복사 해서 하면됨

# 상호작용 가능 - 크게, 단독, 늘리기 가능
streamlit.subheader("대한민국 강수량-데이터프레임(상호작용가능)")
streamlit.dataframe(df)

# 테이블 고정
streamlit.subheader("대한민국 강수량-테이블(상호작용불가)")
streamlit.table(df)

# 차트 요소
streamlit.subheader("꺾은선 차트 생성")
df1 = pd.read_csv("data\공장별_생산현황.csv")

ax = df1.plot()
ax.set_title("공장별 생산현황", fontsize = 20)
ax.set_xlabel("연도별")
ax.set_ylabel("생산량")
fig1 = ax.get_figure()

streamlit.pyplot(fig1)


df2 = pd.read_excel("data\영업팀별_판매현황.xlsx", index_col = '월')
ax = df2.plot.bar(grid=True, figsize=(15,5), rot=0 )
fig2 = ax.get_figure()

streamlit.subheader("막대 차트 생성")
streamlit.pyplot(fig2)