# request, soup
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Copyright
print('Copyright © NAVER Corp. All Rights Reserved.\n쇼핑인사이트 - 쇼핑 분야별 클릭 추이와 분야별 검색어 현황을 확인할 수 있습니다.')

# HTML
html = urlopen("https://datalab.naver.com/")
soup = BeautifulSoup(html, 'html.parser')

# category sel
ul = soup.select_one("ul.select_list")
cates = ul.select('li > a')
for cate in cates:
	cate.get_text()

category = input('쇼핑 분야를 선택해주세요 : ')

# days popular keyword
divs = soup.select('div.keyword_rank')
for dddd in divs:
	# date
	div = dddd.select_one('div.rank_inner > strong.rank_title > span.title_cell')
	date = div.get_text()
	if date == '':
		break
	print('____________')
	print(date)
	div = dddd.select('div.rank_inner > div.rank_scroll > ul > li > a')
	for i in div:
		index = i.select_one('em.num').get_text()
		title = i.select_one('span.title').get_text()
		print(index+'. '+title)
	print('____________\n')