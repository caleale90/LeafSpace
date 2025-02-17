from unittest import TestCase
from unittest.mock import patch, MagicMock

from lib.model.User import User
from lib.userRequests.RandomUser import RandomUser


class TestRandomUser(TestCase):

    @patch('requests.get')  # Mock requests.get
    def test_get(self, mock_get):
        mock_response = {
            "results": [{
                "name": {"first": "John"},
                "location": {"timezone": {"offset": "+8:00"}}
            }]
        }
        mock_get.return_value = MagicMock(json=lambda: mock_response)

        user = RandomUser().get()

        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "John")
        self.assertEqual(user.timeshift, "+8:00")