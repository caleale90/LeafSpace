from lib.api.BeerApi import BeerApi
from lib.builder.BeerBuilder import BeerBuilder
from lib.drinksRequests.DrinkRequest import DrinkRequest


class BeerRequest(DrinkRequest):

    def random_api_call(self):
        return BeerApi('/random').call_api()

    def build_drink(self, response):
        name = response['name']
        tagline = response['tagline']
        image = response['image']
        return BeerBuilder().set_name(name).set_tagline(tagline).set_image(image).build()
