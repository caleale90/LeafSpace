import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from lib.DaytimeCheck import DaytimeCheck


class TestDaytimeCheck(unittest.TestCase):

    @patch("lib.DaytimeCheck.datetime")  # Mock datetime
    def test_is_daytime(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 2, 17, 12, 0, 0)

        checker = DaytimeCheck()

        self.assertTrue(checker.is_daytime("+2:00"))
        self.assertTrue(checker.is_daytime("-4:00"))

        self.assertFalse(checker.is_daytime("+8:00"))
        self.assertFalse(checker.is_daytime("-8:00"))

    def test_parse_offset(self):
        checker = DaytimeCheck()

        self.assertEqual(checker.parse_offset("+3:30"), timedelta(hours=3, minutes=30))
        self.assertEqual(checker.parse_offset("-5:45"), timedelta(hours=-5, minutes=-45))
        self.assertEqual(checker.parse_offset("0:00"), timedelta(hours=0, minutes=0))
