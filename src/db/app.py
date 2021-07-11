from flask import Flask
import csv, json, os

DIRNAME = os.path.dirname(__file__)


#if __name__ == "__main__":
#app.run()
app = Flask(__name__)

@app.route('/')
def functional():
	return 'Server is functional'

@app.route('/api/pokedex/')
def pokedex():
	return 'wow'

@app.route('/api/pokedex/<string:pokemonName>')
def pokemonSearch(pokemonName):
	pokedexFilepath = os.path.join(DIRNAME, 'data/pokedex.csv')
	
	# Sanitize input
	pokemonName = pokemonName.lower()
	with open(pokedexFilepath, 'r', newline='') as file:
		reader = csv.DictReader(file)
		result = list(filter(lambda x: (x['Name'].lower().replace(' ', '-') == pokemonName), reader))
		if result:
			return json.dumps(list(result))
	return 'Pokemon {} not found'.format(pokemonName)

@app.route('/api/pokedex/all')
def all():
	pokedexFilepath = os.path.join(DIRNAME, 'data/pokedex.csv')
	with open(pokedexFilepath, 'r', newline='') as file:
		reader = csv.DictReader(file)
		return json.dumps(list(reader))
	return 'Pokedex not found'