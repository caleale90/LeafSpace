import unittest
from unittest.mock import patch

from lib.drinksRequests.CocktailRequest import CocktailRequest


class TestCocktailRequest(unittest.TestCase):

    @patch('lib.drinksRequests.CocktailRequest.CocktailApi')
    def test_search_by_letter_call(self, mock_cocktail_api):
        mock_cocktail_api.return_value.call_api.return_value = 'api response'

        api_response = CocktailRequest().search_by_letter_call('M')

        self.assertEqual(api_response, 'api response')
        mock_cocktail_api.assert_called_with('/search.php?f=M')

    @patch('lib.drinksRequests.CocktailRequest.CocktailApi')
    def test_search_by_letter_call_strange_char_are_quoted(self, mock_cocktail_api):
        CocktailRequest().search_by_letter_call('ع')

        mock_cocktail_api.assert_called_with('/search.php?f=%D8%B9')

    @patch('lib.drinksRequests.CocktailRequest.CocktailApi')
    def test_random_api_call(self, mock_cocktail_api):
        mock_cocktail_api.return_value.call_api.return_value = 'fake_response'

        cocktail_response = CocktailRequest().random_api_call()

        self.assertEqual(cocktail_response, 'fake_response')

    @patch('lib.drinksRequests.CocktailRequest.CocktailRequest.can_create_drink', return_value=False)
    @patch('lib.drinksRequests.CocktailRequest.CocktailBuilder')
    def test_when_drinks_is_not_in_response(self, mock_cocktail_builder, mock_can_create_drink):
        result = CocktailRequest().build_drink('response')

        mock_cocktail_builder.assert_not_called()
        mock_can_create_drink.assert_called_with('response')

        self.assertIsNone(result)

    def test_can_create_drink(self):
        response = {}
        self.assertFalse(CocktailRequest().can_create_drink(response))

        response = {'drinks': 'valid'}
        self.assertTrue(CocktailRequest().can_create_drink(response))

        response = {'drinks': 'no data found'}
        self.assertFalse(CocktailRequest().can_create_drink(response))
