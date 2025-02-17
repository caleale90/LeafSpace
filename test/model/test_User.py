from unittest import TestCase

from lib.model.User import User


class TestUser(TestCase):
    
    def setUp(self):
        self.user = User('John', 'timeshift')
    
    def test_get_first_letter(self):
        self.assertEqual('j', self.user.get_first_letter())

    def test_get_timeshift(self):
        self.assertEqual('timeshift', self.user.get_timeshift())
