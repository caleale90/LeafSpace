import unittest
from lib.model.Beer import Beer
from lib.builder.BeerBuilder import BeerBuilder


class TestBeerBuilder(unittest.TestCase):

    def test_beer_builder_sets_values_correctly(self):
        builder = BeerBuilder()
        beer = (builder
                .set_name("IPA")
                .set_price(5.99)
                .set_rating_avg(4.2)
                .add_rating_review("Great beer!")
                .set_image("ipa.png")
                .build())

        self.assertIsInstance(beer, Beer)
        self.assertEqual(beer.name, "IPA")
        self.assertEqual(beer.price, 5.99)
        self.assertEqual(beer.rating_avg, 4.2)
        self.assertEqual(beer.rating_reviews, ["Great beer!"])
        self.assertEqual(beer.image, "ipa.png")

    def test_beer_builder_on_missing_name(self):
        builder = BeerBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_price(5.99).build()
        self.assertEqual(str(context.exception), "Name and price are required for a beer")

    def test_beer_builder_on_missing_price(self):
        builder = BeerBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_name("IPA").build()
        self.assertEqual(str(context.exception), "Name and price are required for a beer")
