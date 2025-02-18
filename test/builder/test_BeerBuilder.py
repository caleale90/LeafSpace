import unittest
from lib.model.Beer import Beer
from lib.builder.BeerBuilder import BeerBuilder


class TestBeerBuilder(unittest.TestCase):

    def test_beer_builder_sets_values_correctly(self):
        builder = BeerBuilder()
        beer = (builder
                .set_name('IPA')
                .set_tagline('tagline')
                .set_image('ipa.png')
                .build())

        self.assertIsInstance(beer, Beer)
        self.assertEqual(beer.name, 'IPA')
        self.assertEqual(beer.tagline, 'tagline')
        self.assertEqual(beer.image, 'ipa.png')

    def test_beer_builder_on_missing_name(self):
        builder = BeerBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_tagline('tagline').build()
        self.assertEqual(str(context.exception), 'Name and tagline are required for a beer')

    def test_beer_builder_on_missing_price(self):
        builder = BeerBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_name('IPA').build()
        self.assertEqual(str(context.exception), 'Name and tagline are required for a beer')
