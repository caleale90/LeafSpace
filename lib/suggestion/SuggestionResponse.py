class SuggestionResponse:

    def __init__(self, beer, cocktail):
        self.beer = beer
        self.cocktail = cocktail

    def to_dict(self):
        result = {}
        if self.beer is not None:
            result["beer"] = self.beer.to_dict()
        if self.cocktail is not None:
            result["cocktail"] = self.cocktail.to_dict()
        return result