import urllib.request

# URL과 저장 경로 지정하기
url = "http://imgur.com/ren2RV6.png"
savename = "test.png"

# 다운로드
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다..!")