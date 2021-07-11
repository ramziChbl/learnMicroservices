# Extracts all the data of Pokedex table in the specified URL into 1 csv file 'pokedex.csv'

import csv, requests
from bs4 import BeautifulSoup


BASE_URL = "https://pokemondb.net/pokedex/all"
# CSV header fields
FIELDS = ['Num', 'Image url', 'Name', 'Type1', 'Type2','Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

def parsePokedex(content):
    soupParser = BeautifulSoup(content, "html.parser")
    table = soupParser.find('table', id='pokedex')
    tableBody = table.find('tbody')
    pokedex = []
    for tableLine in tableBody.find_all('tr'):
        pokeInfo = {}
        columns = tableLine.find_all('td')

        pokeInfo['Num'] = columns[0].find_all('span')[2].text
        pokeInfo['Image url'] = tableLine.find(class_='icon-pkmn')['data-src']
        pokeInfo['Name'] = columns[1].a.text
        pokeInfo['Type1'] = columns[2].a.text
        types = columns[2].find_all('a')
        if len(types) > 1:
            pokeInfo['Type2'] = types[1].text
        else:
            pokeInfo['Type2'] = ''

        for i, title in enumerate(FIELDS[5:], start=3):
            pokeInfo[title] = columns[i].text

        pokedex.append(pokeInfo)
    return pokedex

def scrapePage():
    with open('pokedex.csv', 'w', newline='') as csvfile:
        url = BASE_URL
        #response = requests.get(url)
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print("Status:", response.status_code)
        content = response.text
        pokedex = parsePokedex(content)
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(pokedex)
        print('Pokedex extraction complete : wrote {} lines'.format(len(pokedex)))

scrapePage()
