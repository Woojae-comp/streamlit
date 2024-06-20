import streamlit as st
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

# Selenium 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # 브라우저 창이 닫히지 않도록 설정
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def scrape_lyrics(singer):
    # 드라이버 실행
    driver = webdriver.Chrome(options=chrome_options)
    
    # Melon 웹사이트로 이동
    url = 'https://www.melon.com/index.htm'
    driver.get(url)
    
    # 검색창 찾기 및 검색어 입력
    elem = driver.find_element(By.ID, "top_search")
    elem.clear()
    elem.send_keys(singer)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # '앨범' 메뉴를 찾아 클릭
    album = driver.find_element(By.XPATH, '//*[@id="divCollection"]/ul/li[4]/a/span')
    album.click()
    time.sleep(2)
    
    # 첫 번째 앨범의 이미지를 클릭
    driver.find_element(By.XPATH, '//*[@id="frm"]/div/ul/li[1]/div/a[1]').click()
    time.sleep(1)
    
    # 노래 제목과 가사를 저장할 리스트 초기화
    lyrics = []
    stitle = []
    
    # 노래 목록의 tr 요소 개수를 동적으로 계산
    rows = driver.find_elements(By.XPATH, '//*[@id="frm"]/div/table/tbody/tr')
    num_rows = len(rows)
    
    # 동적으로 계산된 개수를 사용하여 노래 제목과 가사 크롤링
    for i in range(1, num_rows + 1):
        try:
            # 노래 제목 찾기
            xp_t = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/div[1]/span/a'
            song_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xp_t))
            ).text
            stitle.append(song_title)
    
            # 노래 가사 찾기
            xp_s = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/a'
            driver.find_element(By.XPATH, xp_s).click()
    
            try:
                lyric = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'd_video_summary'))
                ).text.replace("\n", " ")
                lyrics.append(lyric)
            except TimeoutException:
                lyrics.append("")  # 가사를 찾을 수 없는 경우 빈 문자열 추가
    
            # 이전 페이지로 돌아가기
            driver.back()
            time.sleep(1)
    
        except (TimeoutException, NoSuchElementException) as e:
            st.write(f"Error processing song {i}: {e}")
            # 제목과 가사를 가져오지 못한 경우 빈 값을 추가
            if len(stitle) < i:
                stitle.append("Unknown Title")  # 제목을 찾을 수 없는 경우
            if len(lyrics) < i:
                lyrics.append("")  # 가사를 찾을 수 없는 경우 빈 문자열 추가
    
    # 노래 제목과 가사를 데이터프레임에 저장
    song_data = pd.DataFrame({'노래제목': stitle, '노래가사': lyrics})
    
    # 드라이버 종료
    driver.quit()
    
    return song_data