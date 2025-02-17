from lib.RandomDrinkRequest import RandomDrinkRequest
from lib.api.CocktailApiRequest import CocktailApiRequest
from lib.builder.CocktailBuilder import CocktailBuilder


class RandomCocktailRequest(RandomDrinkRequest):

    def get_random(self):
        response = CocktailApiRequest("https://www.thecocktaildb.com/api/json/v1/1/random.php").call_api()
        return self.build_cocktail(response.json())

    def build_cocktail(self, data):
        if "drinks" in data and data["drinks"]:
            drink = data["drinks"][0]
            name = drink["strDrink"]
            instructions = drink["strInstructions"]
            ingredients = []

            cocktail_builder = CocktailBuilder().set_name(name).set_instructions(instructions)

            self.parse_ingredients(cocktail_builder, drink, ingredients)

            tagline = f"Enjoy the classic taste of {name}!"
            cocktail_builder.set_tagline(tagline)

            return cocktail_builder.build()
        else:
            print("No cocktail found. Try again!")

    @staticmethod
    def parse_ingredients(cocktail_builder, drink, ingredients):
        for i in range(1, 16):
            ingredient = drink.get(f"strIngredient{i}")
            measure = drink.get(f"strMeasure{i}")
            if ingredient:
                ingredients.append(f"{measure.strip() if measure else ''} {ingredient}".strip())
                cocktail_builder.add_ingredient(f"{measure.strip() if measure else ''} {ingredient}".strip())
