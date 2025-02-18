import unittest
from unittest.mock import patch, MagicMock
from app import app


class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.testing = True
        cls.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'response': 'Welcome to the friend bar!'})

    @patch('lib.drinksRequests.CocktailRequest.CocktailRequest.get_random',
           return_value=MagicMock(to_dict=lambda: {'name': 'Mojito'}))
    def test_random_cocktail(self, _mock_cocktail):
        response = self.client.get('/cocktail')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'cocktail': {'name': 'Mojito'}})

    @patch('lib.drinksRequests.CocktailRequest.CocktailRequest.get_random', return_value=None)
    def test_random_cocktail_not_found(self, _mock_cocktail):
        response = self.client.get('/cocktail')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'cocktail': 'no cocktail found'})

    @patch('lib.drinksRequests.BeerRequest.BeerRequest.get_random',
           return_value=MagicMock(to_dict=lambda: {'name': 'IPA'}))
    def test_random_beer(self, _mock_beer):
        response = self.client.get('/beer')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'beer': {'name': 'IPA'}})

    @patch('lib.drinksRequests.BeerRequest.BeerRequest.get_random', return_value=None)
    def test_random_beer_not_found(self, _mock_beer):
        response = self.client.get('/beer')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'beer': 'no beer found'})

    @patch('lib.suggestion.Suggestion.Suggestion.get_recommendation',
           return_value=MagicMock(to_dict=lambda: {'drink': 'Margarita'}))
    def test_get_suggestion(self, _mock_suggestion):
        response = self.client.get('/suggestion')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'suggestion': {'drink': 'Margarita'}})
