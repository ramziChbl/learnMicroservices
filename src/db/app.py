from flask import Flask, Response
import csv, json, os

DIRNAME = os.path.dirname(__file__)


app = Flask(__name__)

@app.route('/')
def functional():
	# 204 : The server has fulfilled the request but does not need to return a response body.
	status_code = Response(status=204)
	return status_code

@app.route('/api/pokedex/<string:pokemonName>')
def pokemonSearch(pokemonName):
	pokedexFilepath = os.path.join(DIRNAME, 'data/pokedex.csv')
	
	# Sanitize input (I don't think I'll need to strip it, might change later)
	pokemonName = pokemonName.lower()

	with open(pokedexFilepath, 'r', newline='') as file:
		reader = csv.DictReader(file)
		result = list(filter(lambda x: (x['Name'].lower().replace(' ', '-') == pokemonName), reader))
		print(result)
		if result:
			return json.dumps(list(result))
		else: # No pokemon matches the input name
			print('no matches, in else')
			# 400 Bad Request – This means that client-side input fails validation.
			status_code = Response(status=400)
			return status_code
	# 500 Internal server error : couldn't find db file
	status_code = Response(status=500)
	return status_code

@app.route('/api/pokedex', strict_slashes=False)
@app.route('/api/pokedex/all', strict_slashes=False)
def all():
	pokedexFilepath = os.path.join(DIRNAME, 'data/pokedex.csv')
	with open(pokedexFilepath, 'r', newline='') as file:
		reader = csv.DictReader(file)
		return json.dumps(list(reader))

	# 500 Internal server error : couldn't find db file
	status_code = Response(status=500)
	return status_code

if __name__ == "__main__":
    app.run(port=5002)