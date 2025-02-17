from lib.model.Cocktail import Cocktail


class CocktailBuilder:
    def __init__(self):
        self.name = None
        self.tagline = None
        self.instructions = None
        self.ingredients = []

    def set_name(self, name):
        self.name = name
        return self

    def set_tagline(self, tagline):
        self.tagline = tagline
        return self

    def set_instructions(self, instructions):
        self.instructions = instructions
        return self

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self

    def build(self):
        if not self.name or not self.instructions:
            raise ValueError("Name and instructions are required for a cocktail")
        return Cocktail(self.name, self.tagline, self.instructions, self.ingredients)