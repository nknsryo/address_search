import requests

# zipcode = input("郵便番号を入力してください(ハイフン無し7桁) >> :")
zipcode = "4443174"
url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
response = requests.get(url)
print(response)
print(response.text)
