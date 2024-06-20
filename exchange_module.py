import pandas as pd
import warnings
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO # 이미지나 excel 파일, text 파일 제외한 파일은 이런식으로 해야됨 


# BeautifulSoup 경고 무시 설정
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def ex_rate():
    def get_exchange(national):
        lastpagenum = 10
        df = pd.DataFrame()
        for pagenum in range(1, lastpagenum + 1):
            url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{national}KRW&page={pagenum}"
            dfs = pd.read_html(url, encoding='cp949', header=1)  # header=1로 설정하여 첫 번째 줄을 헤더로 사용
            if dfs[0].empty:
                if pagenum == 1:
                    print(f"통화코드 {national} Error")
                else:
                    print(f"마지막 페이지는 {pagenum - 1} 입니다.")
                break
            df = pd.concat([df, dfs[0]], ignore_index=True)
        # df.index = range(1, len(df) + 1)
        return df

    currency_name_dict = {"미국 달러":"USD", "유로화":"EUR", "엔화" : "JPY"}
    currency_name = st.selectbox("통화선택", currency_name_dict.keys())
    clicked = st.button("환율데이터 가져오기")

    if clicked: # True 면 생략 가능
        national = currency_name_dict[currency_name]
        get_exchange(national)
        df_exchange = get_exchange(national)

        # 환율 데이터
        st.subheader(f"{currency_name} 환율 데이터")
        # st.dataframe(df_exchange)

        df_exchange = df_exchange.drop(columns=['전일대비'])
        df_exchange['날짜'] = pd.to_datetime(df_exchange['날짜'], format="%Y.%m.%d", errors="ignore").dt.date
        df_exchange = df_exchange.set_index('날짜')

        st.dataframe(df_exchange)

        # 그래프 설정 및 출력
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'  
        ax = df_exchange['매매기준율'].plot(figsize=(15, 5), grid=True)
        ax.set_title(f"{currency_name} 환율 매매기준율 그래프", fontsize=25)
        ax.set_xlabel("기간", fontsize=15)
        ax.set_ylabel("매매기준율", fontsize=15)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        fig = ax.get_figure()
        st.pyplot(fig)

        # 파일 다운로드 
        st.text("** 환율 데이터 다운로드 **")

        
        csv_data = df_exchange.to_csv(index=True) # 뒤에 파일이름 적으면 로컬에 저장

        # 바이너리 파일로 넣었다가 excel파일로 컨버트해줘야함
        excel_data = BytesIO() # 메모리 버퍼(임시장소에 바이너리 객체 생성)
        df_exchange.to_excel(excel_data)
        # 엑셀 형식으로 버퍼에 쓰기

        col1, col2 = st.columns(2)
        with col1:
            st.download_button("CSV 파일 다운로드", csv_data, file_name="exchangedata.csv")
        with col2:
            st.download_button("Excel 파일 다운로드", excel_data, file_name="exchangedata.xlsx")

    else:
        pass



