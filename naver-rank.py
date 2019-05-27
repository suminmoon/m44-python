# naver 에서 html 파일을 가지고 온다.
# Beatifulsoup을 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.

import requests
import bs4

url = 'http://www.naver.com'
response = requests.get(url).text
soup = bs4.BeautifulSoup(response, 'html.parser')
results = soup.find_all('span',class_='ah_k')
index = 0
for result in results:
  index = index +1
  print(index, result.text)