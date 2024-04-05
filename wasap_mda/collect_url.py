import requests
from bs4 import BeautifulSoup

url = "https://www.promiedos.com.ar/club=17"


def main():

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    tables = soup.find_all("table", class_="fixclub")
    matches = tables[0].find_all("tr")

    data = []
    for match in matches:

        data_match = []
        for _loc in match.children:

            data_match.append(_loc.text)
        print('-' * 50)
        data.append(data_match)

    for x in data:
        print(f'Partido: {x}')


if __name__ == "__main__":
    print('-' * 50)
    print('-' * 50)
    print('-' * 50)

    main()
