from search_address import search_address


def main():
    zipcode = "4443174"

    address = search_address(zipcode)

    assert "愛知県岡崎市真伝町" == address


if __name__ == '__main__':
    main()
