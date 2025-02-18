from unittest import TestCase

from lib.model.Beer import Beer


class TestBeer(TestCase):

    def test_to_dict(self):
        expected = {'name': 'name',
                    'tagline': 'tagline',
                    'image': 'image'}
        result = Beer('name', 'tagline', 'image').to_dict()
        self.assertDictEqual(expected, result)
