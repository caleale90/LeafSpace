import unittest
from unittest.mock import patch

from lib.api.Api import Api
from lib.api.CocktailApi import CocktailApi


class TestCocktailApi(unittest.TestCase):

    @patch.object(Api, '__init__', return_value=None)
    def test_cocktail_api_initialization(self, mock_api_init):
        base_url = "https://cocktailapi.com"
        beer_api = CocktailApi(base_url)

        mock_api_init.assert_called_once_with(base_url)
        self.assertIsInstance(beer_api, CocktailApi)
