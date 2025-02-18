import unittest

from lib.model.Beer import Beer
from lib.model.Cocktail import Cocktail
from lib.suggestion.SuggestionResponse import SuggestionResponse


class TestSuggestionResponse(unittest.TestCase):

    def test_to_dict_when_no_cocktail_and_beer(self):
        expected = {'beer': 'no beer it\'s daytime', 'cocktail': 'no cocktail found'}

        beer = None
        cocktail = None
        result = SuggestionResponse(beer, cocktail).to_dict()

        self.assertDictEqual(result, expected)

    def test_to_dict(self):
        expected = {'beer': {'image': 'image',
                             'name': 'name',
                             'tagline': 'tagline'},
                    'cocktail': {'name': 'name',
                                 'tagline': 'tagline',
                                 'instructions': 'ins',
                                 'ingredients': 'ingredients'}}

        beer = Beer('name', 'tagline', 'image')
        cocktail = Cocktail('name', 'tagline', 'ins', 'ingredients')
        result = SuggestionResponse(beer, cocktail).to_dict()

        self.assertDictEqual(result, expected)
