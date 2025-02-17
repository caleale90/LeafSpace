import json


class Cocktail:

    def __init__(self, name, tagline, instructions, ingredients):
        self.name = name
        self.tagline = tagline
        self.instructions = instructions
        self.ingredients = ingredients

    def to_dict(self):
        return {
            "name": self.name,
            "tagline": self.tagline,
            "instructions": self.instructions,
            "ingredients": self.ingredients
        }

    def __str__(self):
        return json.dumps(self.to_dict())
