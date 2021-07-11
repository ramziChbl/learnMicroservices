from flask import Flask
import csv, json


#if __name__ == "__main__":
#app.run()
app = Flask(__name__)

@app.route('/')
def functional():
	return 'Server is functional'

@app.route('/api/pokedex/')
def pokedex():
	return 'wow'


@app.route('/api/pokedex/<int:generation>/<int:pokemonNumber>')
def pokemon(generation, pokemonNumber):
	if generation not in range(1,9):
		return 'Wrong generation'
	print((generation, pokemonNumber))
	print('data/gen{}.csv'.format(int(generation)))
	with open('data/gen{}.csv'.format(int(generation))) as file:
		print('IM in')
		reader = csv.DictReader(file)
		print(reader)
		for row in reader:
			print(row)
			if int(row['Num']) == pokemonNumber:
				print(row)
				return json.dumps(row)
	return 'not found'

@app.route('/api/pokedex/<int:generation>/<int:pokemonNumber>/<string:field>')
def field(generation, pokemonNumber, field):
	if generation not in range(1,9):
		return 'Wrong generation'
	print((generation, pokemonNumber))
	print('data/gen{}.csv'.format(int(generation)))
	with open('data/gen{}.csv'.format(int(generation))) as file:
		print('IM in')
		reader = csv.DictReader(file)
		print(reader)
		for row in reader:
			print(row)
			if int(row['Num']) == pokemonNumber:
				if row[field]:
					return json.dumps(row[field])
				break
	return 'not found'


#	app = Flask(__name__)

