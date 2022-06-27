print('잠깐씩 프로그램이 멈출 때는, 아무 키나 눌러주세요 ..\n')
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

# open wd
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('headless')
options.add_argument('window-size=1920, 1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver\chromedriver.exe', options=options)
sleep(1)

# get url
url='https://datalab.naver.com/'
driver.get(url)
sleep(1)

# category button click
elem=driver.find_element(By.CLASS_NAME, 'select_btn')
elem.click()

# print cates
elem=driver.find_elements(By.CLASS_NAME, 'option')
for i in range(12):
	print(str(i)+'.',elem[i].text)
sleep(1)

# cate input, click it !
u_cate=int(input('\n검색 분야의 인덱스 입력 : '))
category=elem[u_cate].text
elem[u_cate].click()
sleep(1)

# print keywords ..
rank_inners=driver.find_elements(By.CLASS_NAME, 'keyword_rank')
print('지난 4일간의 '+category+' 분야의 인기 검색어 리스트입니다.')
for rk in rank_inners:
	if(rk.text!=''):
		print('_______________')
		print(rk.text)
		print('_______________\n')

# input keyword
key=input('검색어를 입력하세요(str) : ')

# url fix
url+='shoppingInsight/sKeyword.naver?keyword='+key
driver.get(url)
sleep(1)

# download screenshot
category=category.replace('/', ', ')

png_name='지난 한 달간 '+category+'분야의 '+key+' 검색어 클릭량 추이'+'.png'

chart=driver.find_element(By.CLASS_NAME, 'inner_graph_area')
chart.screenshot(png_name)


print("'"+os.getcwd()+'\\'+png_name+"'", '\n위치에 파일이 저장되었습니다 .')

driver.quit()

sleep(10)