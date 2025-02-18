import unittest
from unittest.mock import patch

from lib.drinksRequests.BeerRequest import BeerRequest
from lib.model.Beer import Beer


class TestCocktailRequest(unittest.TestCase):

    @patch('lib.drinksRequests.BeerRequest.BeerApi')
    def test_random_api_call(self, mock_beer_api):
        mock_beer_api.return_value.call_api.return_value = 'fake_response'

        beer_request = BeerRequest()

        self.assertEqual(beer_request.random_api_call(), 'fake_response')


    def test_build_drink(self):
        response = {'name': 'beer', 'tagline': 'tagline', 'image': 'image'}
        beer = BeerRequest().build_drink(response)

        self.assertEqual(beer.name, 'beer')
        self.assertEqual(beer.tagline, 'tagline')
        self.assertEqual(beer.image, 'image')
        self.assertIsInstance(beer, Beer)
