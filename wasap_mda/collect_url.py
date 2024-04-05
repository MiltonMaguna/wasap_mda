import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.promiedos.com.ar/club=17"


def collect_url():

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    tables = soup.find_all("table", class_="fixclub")
    matches = tables[0].find_all("tr")

    data_table = []
    for match in matches:

        data_match = []

        for _loc in match.children:

            data_match.append(_loc.text)

        data_table.append(data_match)

    return data_table
    # for x in data_table:
    #     print(f'Partido: {x}')


def create_table(data: list):

    # columns = data[0]
    columns = ["Fecha", "Numero de Fecha", "Local/Visitante",
               "Rival", "Resultado", "Ficha"]

    data.pop(0)
    return pd.DataFrame(data, columns=columns)


if __name__ == "__main__":
    print('-' * 50)
    print('-' * 50)

    data = collect_url()
    df = create_table(data)
    print(df)
