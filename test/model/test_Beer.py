from unittest import TestCase

from lib.model.Beer import Beer


class TestBeer(TestCase):

    def test_to_dict(self):
        expected = {'name': 'name',
                    'price': 'price',
                    'rating_avg': 'avg_rating',
                    'rating_reviews': ['rev1', 'rev2'],
                    'image': 'image'}
        result = Beer('name', 'price', 'avg_rating', ['rev1', 'rev2'], 'image').to_dict()
        self.assertDictEqual(expected, result)
