from lib.DaytimeCheck import DaytimeCheck
from lib.drinksRequests.BeerRequest import BeerRequest
from lib.userRequests.RandomUser import RandomUser


class Suggestion:

    def get_recommendation(self):
        user = RandomUser().get()
        response = {}

        if DaytimeCheck.is_daytime(user.get_timeshift()):
            response['beer'] = BeerRequest().get_random()

        # TODO: devo ripartire dalla richiesta per avere i cocktail che iniziano per la prima lettera
        response['cocktail'] = ''

