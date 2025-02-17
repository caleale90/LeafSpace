from unittest import TestCase

from lib.model.Cocktail import Cocktail


class TestCocktail(TestCase):

    def test_to_dict(self):
        expected = {
            "name": 'name',
            "tagline": 'tagline',
            "instructions": 'instructions',
            "ingredients": ['ing1', 'ing2']
        }
        result = Cocktail('name', 'tagline', 'instructions', ['ing1', 'ing2']).to_dict()
        self.assertDictEqual(expected, result)
