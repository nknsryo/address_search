import requests


def main():
    # zipcode = input("郵便番号を入力してください(ハイフン無し7桁) >> :")
    zipcode = "4443174"
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    results = response.json()['results']

    pref_name = results[0]['address1']
    city_name = results[0]['address2']
    town_name = results[0]['address3']

    return f"{pref_name}{city_name}{town_name}"


# print(main())

if __name__ == "__main__":
    main()
