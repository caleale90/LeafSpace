import unittest
from unittest.mock import patch

from lib.api.Api import Api
from lib.api.CocktailApi import CocktailApi


class TestCocktailApi(unittest.TestCase):

    @patch.object(Api, '__init__', return_value=None)
    def test_cocktail_api_initialization(self, mock_api_init):
        base_url = "/endpoint"
        beer_api = CocktailApi(base_url)

        mock_api_init.assert_called_once_with('https://www.thecocktaildb.com/api/json/v1/1/endpoint')
        self.assertIsInstance(beer_api, CocktailApi)
