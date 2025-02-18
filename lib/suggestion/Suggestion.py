import concurrent.futures

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
        print(f"User first letter: {user.get_first_letter()}")
        daytime = DaytimeCheck().is_daytime(user.get_timeshift())
        print(f"Is Daytime: {daytime}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            beer_future = executor.submit(BeerRequest().get_random) if daytime else None
            cocktail_future = executor.submit(CocktailRequest().search_by_letter, user.get_first_letter())

            self.beer = beer_future.result() if beer_future else None
            self.cocktail = cocktail_future.result()

        return SuggestionResponse(self.beer, self.cocktail)
