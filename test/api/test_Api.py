import unittest
from unittest.mock import patch, MagicMock

from lib.api.Api import Api


class TestApi(unittest.TestCase):

    @patch('requests.get')  # Mock requests.get
    def test_call_api_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"message": "Success"}'
        mock_get.return_value = mock_response

        api = Api("https://example.com")
        response = api.call_api()

        mock_get.assert_called_once_with("https://example.com")  # Ensure correct API call
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{"message": "Success"}')
