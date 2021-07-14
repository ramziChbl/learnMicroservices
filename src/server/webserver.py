from flask import Flask
import os, requests, json
from requests import HTTPError
import pprint
from collections import OrderedDict

FIELDS = ['Num', 'Image url', 'Name', 'Type1', 'Type2','Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

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
        print('conncection established')
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        decodedResponse = json.loads(response.text)
        print(len(decodedResponse))
        #print(decodedResponse)
        pprint.pprint(decodedResponse)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print("Status:", response.status_code)
    #return render_template('pokedex.html')
    return 'lol'

if __name__ == "__main__":
    app.run(port=5001)