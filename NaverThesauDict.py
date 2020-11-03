import requests
from bs4 import BeautifulSoup

import lxml
##requests, bs4, lxml 설치 필요


print("검색하려는 영어 단어를 입력하세요.")
word = input()

url1 = "http://endic.naver.com/search.nhn?query=" + word
url2 = "https://www.thesaurus.com/browse/" + word
response1 = requests.get(url1)
response2 = requests.get(url2)
soup1 = BeautifulSoup(response1.content, "lxml")
soup2 = BeautifulSoup(response2.content, "lxml")

wordclass = ""
result = ""
syn1 = ""
syn2 = ""
try:
    wordclass += soup1.find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k09'}).get_text()
    result += soup1.find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k05'}).get_text()
except:
    wordclass = "네이버 사전에 등재되어 있지 않습니다."
    result = "네이버 사전에 등재되어 있지 않습니다."

try:
    syn1 += soup2.find('a',{'class':'css-1s3v085 eh475bn1'}).get_text()
    syn2 += soup2.find('a',{'class':'css-1wndipq eh475bn1'}).get_text()
except:
    syn1 = "Thesaurus에 등재되어 있지 않습니다."
    syn2 = "Thesaurus에 등재되어 있지 않습니다."


print("품사 : " + wordclass)
print("뜻: " + result)
print("유의어 1 : " + syn1)
print("유의어 2 : " + syn2)