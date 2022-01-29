import requests

url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=4443174"
response = requests.get(url)
print(response)
print(response.text)
