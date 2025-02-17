import unittest
from unittest.mock import patch
from lib.api.Api import Api
from lib.api.BeerApi import BeerApi  # Ensure correct import path

class TestBeerApi(unittest.TestCase):

    @patch.object(Api, '__init__', return_value=None)
    def test_beer_api_initialization(self, mock_api_init):
        base_url = "https://beerapi.com"
        beer_api = BeerApi(base_url)

        mock_api_init.assert_called_once_with(base_url)
        self.assertIsInstance(beer_api, BeerApi)
