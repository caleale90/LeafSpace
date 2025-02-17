import json

from lib.drinksRequests.DrinkRequest import DrinkRequest
from lib.builder.BeerBuilder import BeerBuilder


class BeerRequest(DrinkRequest):

    def random_api_call(self):
        # response = BeerApiRequest("https://api.sampleapis.com/beers/ale").call_api()
        # TODO: rimuovere quando andranno le API e scommentare riga sopra

        return FakeObject("Birra fresca", 11)

    def build_drink(self, response):
        return BeerBuilder().set_name("Birra fresca").set_price(11).set_image("wonderful_img.jpg").set_rating_avg(
            3.5).add_rating_review("a good review").add_rating_review("a bad review").build()

# TODO: rimuovere quando andranno le API
class FakeObject:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return json.dumps(self.__dict__, indent=4)