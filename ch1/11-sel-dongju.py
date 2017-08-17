from bs4 import BeautifulSoup
import urllib.request as req

# 뒤의 인코딩 부분은 "저자:윤동주"라는 의미
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# html 내 태그 선택
a_lsit = soup.select("#mw-content-text > div > ul > li > b > a")

for a in a_lsit:
    name = a.string
    print("-", name)