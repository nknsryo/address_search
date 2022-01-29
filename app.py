from search_address import search_address


def main():
    zipcode = input("郵便番号を入力してください(ハイフン無し7桁) >> :")
    # zipcode = "4443174"
    address = search_address(zipcode)
    print(address)


if __name__ == "__main__":
    main()
