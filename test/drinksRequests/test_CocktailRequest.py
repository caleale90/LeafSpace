import unittest
from unittest.mock import patch, MagicMock

from lib.drinksRequests.CocktailRequest import CocktailRequest


class TestCocktailRequest(unittest.TestCase):

    @patch('lib.drinksRequests.CocktailRequest.CocktailApi.call_api', return_value='api response')
    def test_search_by_letter(self, mock_cocktail_call_api):
        api_response = CocktailRequest().search_by_letter('M')

        self.assertEqual(api_response, 'api response')
        mock_cocktail_call_api.assert_called()


    @patch('lib.drinksRequests.CocktailRequest.CocktailRequest.build_drink', return_value='a drink')
    @patch('lib.drinksRequests.CocktailRequest.CocktailApi')
    def test_search_by_letter_strange_char_are_quoted(self, mock_cocktail_api, mock_build_drink):
        mock_response = MagicMock()
        mock_response.json.return_value = 'fake_response'

        mock_cocktail_api.return_value.call_api.return_value = mock_response

        CocktailRequest().search_by_letter('ع')

        mock_cocktail_api.assert_called_with('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=%D8%B9')


    @patch('lib.drinksRequests.CocktailRequest.CocktailApi')
    def test_random_api_call(self, mock_cocktail_api):

        mock_cocktail_api.return_value.call_api.return_value = 'fake_response'

        cocktail_request = CocktailRequest()

        self.assertEqual(cocktail_request.random_api_call(), 'fake_response')


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
