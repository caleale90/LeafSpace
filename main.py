from flask import Flask, jsonify

from lib.RandomCocktailRequest import RandomCocktailRequest

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Benvenuto nella mia app Flask!</h1>"

@app.route('/cocktail')
def random_cocktail():
    cocktail = RandomCocktailRequest.get_random_cocktail()
    return jsonify({"cocktail": cocktail.to_dict()}), 200


if __name__ == '__main__':
    app.run(debug=True)
