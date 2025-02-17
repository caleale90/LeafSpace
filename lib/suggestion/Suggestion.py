from lib.DaytimeCheck import DaytimeCheck
from lib.drinksRequests.BeerRequest import BeerRequest
from lib.drinksRequests.CocktailRequest import CocktailRequest
from lib.suggestion.SuggestionResponse import SuggestionResponse
from lib.userRequests.RandomUser import RandomUser


class Suggestion:

    def __init__(self):
        self.beer = None
        self.cocktail = None

    def get_recommendation(self):
        user = RandomUser().get()

        if DaytimeCheck().is_daytime(user.get_timeshift()):
            self.beer = BeerRequest().get_random()

        print(f"User first letter: {user.get_first_letter()}")
        self.cocktail = CocktailRequest().search_by_letter(user.get_first_letter())
        return SuggestionResponse(self.beer, self.cocktail)

