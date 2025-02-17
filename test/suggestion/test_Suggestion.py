import unittest
from unittest.mock import patch, MagicMock

from lib.suggestion.Suggestion import Suggestion
from lib.suggestion.SuggestionResponse import SuggestionResponse


class TestSuggestion(unittest.TestCase):

    @patch("lib.suggestion.Suggestion.RandomUser")
    @patch("lib.suggestion.Suggestion.BeerRequest")
    @patch("lib.suggestion.Suggestion.CocktailRequest")
    @patch("lib.suggestion.Suggestion.DaytimeCheck")
    def test_get_recommendation_on_daytime(self, mock_daytime_check, mock_cocktail_request, mock_beer_request,
                                           mock_random_user):
        mock_user = MagicMock()
        mock_user.get_timeshift.return_value = "+2:00"
        mock_user.get_first_letter.return_value = "M"
        mock_random_user.return_value.get.return_value = mock_user

        mock_daytime_check.return_value.is_daytime.return_value = True

        mock_beer = MagicMock()
        mock_beer.name = "IPA"
        mock_beer_request.return_value.get_random.return_value = mock_beer

        mock_cocktail = MagicMock()
        mock_cocktail.name = "Mojito"
        mock_cocktail_request.return_value.search_by_letter.return_value = mock_cocktail

        suggestion = Suggestion()
        result = suggestion.get_recommendation()

        self.assertIsInstance(result, SuggestionResponse)
        self.assertEqual(result.beer.name, "IPA")
        self.assertEqual(result.cocktail.name, "Mojito")  # cocktail should be recommended

        mock_random_user.return_value.get.assert_called_once()
        mock_daytime_check.return_value.is_daytime.assert_called_once_with("+2:00")
        mock_beer_request.return_value.get_random.assert_called_once()
        mock_cocktail_request.return_value.search_by_letter.assert_called_once_with("M")

    @patch("lib.suggestion.Suggestion.RandomUser")
    @patch("lib.suggestion.Suggestion.BeerRequest")
    @patch("lib.suggestion.Suggestion.CocktailRequest")
    @patch("lib.suggestion.Suggestion.DaytimeCheck")
    def test_get_recommendation_on_daytime(self, mock_daytime_check, mock_cocktail_request, mock_beer_request,
                                           mock_random_user):
        mock_user = MagicMock()
        mock_user.get_timeshift.return_value = "+2:00"
        mock_user.get_first_letter.return_value = "M"
        mock_random_user.return_value.get.return_value = mock_user

        mock_daytime_check.return_value.is_daytime.return_value = False

        mock_beer = MagicMock()
        mock_beer.name = "IPA"
        mock_beer_request.return_value.get_random.return_value = mock_beer

        mock_cocktail = MagicMock()
        mock_cocktail.name = "Mojito"
        mock_cocktail_request.return_value.search_by_letter.return_value = mock_cocktail

        suggestion = Suggestion()
        result = suggestion.get_recommendation()

        self.assertIsInstance(result, SuggestionResponse)
        self.assertIsNone(result.beer)
        self.assertEqual(result.cocktail.name, "Mojito")

        mock_random_user.return_value.get.assert_called_once()
        mock_daytime_check.return_value.is_daytime.assert_called_once_with("+2:00")
        mock_beer_request.return_value.get_random.assert_not_called()
        mock_cocktail_request.return_value.search_by_letter.assert_called_once_with("M")

