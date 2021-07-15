from flask import Flask, render_template
import os, requests, json
from requests import HTTPError

DIRNAME = os.path.dirname(__file__)
#DB_HOSTNAME = 'db'
DB_HOSTNAME = 'localhost'
DB_PORT = 5002

app = Flask(__name__)


@app.route('/')
def main():
    # Check if server is alive
    try:
        checkIfAlive = requests.get("http://{}:{}/").format(DB_HOSTNAME, DB_PORT)
    except Exception as e:
        return "DB server unreachable."
    else:
        print("Status:", checkIfAlive.status_code)

    url = "http://{}:{}/api/pokedex".format(DB_HOSTNAME, DB_PORT) 
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print('connection to db established')

        pokedex = json.loads(response.text)

        tableFields = pokedex[0].keys()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print("Status:", response.status_code)

    return render_template('pokedex.html', tableFields = tableFields, pokedex=pokedex)

@app.route('/<string:pokemonName>')
def pokemonDetails(pokemonName):

    url = "http://{}:{}/api/pokedex/{}".format(DB_HOSTNAME, DB_PORT, pokemonName) 
    try:
        response = requests.get(url)
        print(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print('connection to DB established')

        # It can return 2 pokemons if there is a special version of it
        pokemonList = json.loads(response.text)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        if http_err.response.status_code == 400:
            return 'Pokemon \'{}\' not found.\n'.format(pokemonName)
        elif http_err.response.status_code == 500:
            return 'Problem in DB server.'
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return 'lol'
    else:
        print("Status:", response.status_code)

    return render_template('pokemon_details.html', pokemonList=pokemonList)

if __name__ == "__main__":
    app.run(port=5001)