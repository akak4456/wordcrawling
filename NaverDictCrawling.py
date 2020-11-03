import requests
from bs4 import BeautifulSoup
import traceback

import lxml
##requests, bs4, lxml 설치 필요


print("검색하려는 영어 단어를 입력하세요.")
word = input()

url = "http://en.dict.naver.com/#/search?range=all&query=" + word
print(url)
response = requests.get(url)
print(response)
print(response.content)
soup = BeautifulSoup(response.content, "lxml")

wordclass = ""
result = ""
try:
    wordclass += soup.find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k09'}).get_text()
    result += soup.find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k05'}).get_text()
except:
    traceback.print_exc()
    result = "네이버 사전에 등재되어 있지 않습니다."

print(wordclass)
print(result)
