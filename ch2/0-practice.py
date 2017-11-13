import requests

url = "http://www.hanbit.co.kr/member/login_proc.php"
data = {
    "return_url": "http://www.hanbit.co.kr/index.html",
    "m_id": "sellaboo",
    "m_passwd": "boo124578"
}
session = requests.session()
response = session.post(url, data=data)
response.raise_for_status()
print( response.text)