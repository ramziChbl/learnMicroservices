import csv, requests
from bs4 import BeautifulSoup

import aiohttp
import asyncio


BASE_URL = "https://pokemondb.net/pokedex/stats/gen"
# CSV header fields
FIELDS = ['Num', 'Image url', 'Name', 'Type1', 'Type2','Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

def parsePokedex(table):
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

async def scrapePage(num):
	with open('gen{}.csv'.format(num), 'w', newline='') as csvfile:
		url = BASE_URL + str(num)
		content = None
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				print("Status:", response.status)
				content = await response.text()
				
		soupParser = BeautifulSoup(content, "html.parser")
		table = soupParser.find('table', id='pokedex')
		pokedex = parsePokedex(table)

		writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
		writer.writeheader()
		writer.writerows(pokedex)
	print('Gen {} extraction complete'.format(num))


loop = asyncio.get_event_loop()
coroutines = [scrapePage(i) for i in range(1,9)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
