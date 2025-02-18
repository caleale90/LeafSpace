from flask import Flask, jsonify

from lib.drinksRequests.BeerRequest import BeerRequest
from lib.drinksRequests.CocktailRequest import CocktailRequest
from lib.suggestion.Suggestion import Suggestion

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'response': 'Welcome to the friend bar!'})

@app.route('/cocktail')
def random_cocktail():
    cocktail = CocktailRequest().get_random()
    if cocktail:
        return jsonify({'cocktail': cocktail.to_dict()}), 200
    else:
        return jsonify({'cocktail': 'no cocktail found'}), 404

@app.route('/beer')
def random_beer():
    beer = BeerRequest().get_random()
    if beer:
        return jsonify({'beer': beer.to_dict()}), 200
    else:
        return jsonify({'beer': 'no beer found'}), 404

@app.route('/suggestion')
def get_suggestion():
    suggestion = Suggestion().get_recommendation()
    return jsonify({'suggestion': suggestion.to_dict()}), 200


if __name__ == '__main__':
    app.run(debug=True)
