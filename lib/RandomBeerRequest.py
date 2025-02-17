from lib.RandomDrinkRequest import RandomDrinkRequest
from lib.builder.BeerBuilder import BeerBuilder


class RandomBeerRequest(RandomDrinkRequest):

    def get_random(self):
        # response = BeerApiRequest("https://api.sampleapis.com/beers/ale").call_api()
        return self.build()

    def build(self):
        return BeerBuilder().set_name("Birra fresca").set_price(11).set_image("wonderful_img.jpg").set_rating_avg(
            3.5).add_rating_review("a good review").add_rating_review("a bad review").build()
