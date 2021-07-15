from flask import Flask, render_template
import os, requests, json
from requests import HTTPError

DIRNAME = os.path.dirname(__file__)
#DB_HOSTNAME = 'db'
DB_HOSTNAME = 'localhost'

app = Flask(__name__)


@app.route('/')
def main():
    url = "http://{}:5000/api/pokedex/all".format(DB_HOSTNAME) 
    #response = requests.get(url)
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

if __name__ == "__main__":
    app.run(port=5001)