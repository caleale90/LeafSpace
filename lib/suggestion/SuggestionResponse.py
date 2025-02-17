class SuggestionResponse:

    def __init__(self, beer, cocktail):
        self.beer = beer
        self.cocktail = cocktail

    def to_dict(self):
        return {
            "beer": self.beer.to_dict() if self.beer is not None else 'no beer it\'s daytime',
            "cocktail": self.cocktail.to_dict() if self.cocktail is not None else 'no cocktail found'
        }