from urllib.parse import quote

from lib.drinksRequests.DrinkRequest import DrinkRequest
from lib.api.CocktailApi import CocktailApi
from lib.builder.CocktailBuilder import CocktailBuilder


class CocktailRequest(DrinkRequest):

    def search_by_letter_call(self, letter):
        return CocktailApi(f'/search.php?f={quote(letter)}').call_api()

    def random_api_call(self):
        return CocktailApi('/random.php').call_api()

    def build_drink(self, response):
        if self.can_create_drink(response):
            drink = response['drinks'][0]
            name = drink['strDrink']
            instructions = drink['strInstructions']
            ingredients = []

            cocktail_builder = CocktailBuilder().set_name(name).set_instructions(instructions)

            self.parse_ingredients(cocktail_builder, drink, ingredients)

            tagline = f'Enjoy the classic taste of {name}!'
            cocktail_builder.set_tagline(tagline)

            return cocktail_builder.build()
        else:
            return None

    @staticmethod
    def can_create_drink(response):
        return 'drinks' in response and response['drinks'] and response['drinks'] != 'no data found'

    @staticmethod
    def parse_ingredients(cocktail_builder, drink, ingredients):
        for i in range(1, 16):
            ingredient = drink.get(f'strIngredient{i}')
            measure = drink.get(f'strMeasure{i}')
            if ingredient:
                ingredients.append(f'{measure.strip() if measure else ''} {ingredient}'.strip())
                cocktail_builder.add_ingredient(f'{measure.strip() if measure else ''} {ingredient}'.strip())


