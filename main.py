from flask import Flask, jsonify

from lib.drinksRequests.BeerRequest import BeerRequest
from lib.drinksRequests.CocktailRequest import CocktailRequest
from lib.suggestion.Suggestion import Suggestion

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the friend bar!</h1>"

@app.route('/cocktail')
def random_cocktail():
    cocktail = CocktailRequest().get_random()
    return jsonify({"cocktail": cocktail.to_dict()}), 200

@app.route('/beer')
def random_beer():
    beer = BeerRequest().get_random()
    return jsonify({"beer": beer.to_dict()}), 200

@app.route('/suggestion')
def get_suggestion():
    suggestion = Suggestion().get_recommendation()
    return jsonify({"suggestion": suggestion.to_dict()}), 200


if __name__ == '__main__':
    app.run(debug=True)
