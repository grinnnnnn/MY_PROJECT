import requests

r = requests.get("https://naver.com")
print(r.status_code)
