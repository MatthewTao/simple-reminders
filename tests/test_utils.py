from src.utils import next_day_of_week

from datetime import datetime
import unittest


class TestUtils(unittest.TestCase):

    def test_next_day_of_week(self):
        now = datetime.now()
        next_monday = next_day_of_week(0, now)
        print(next_monday)
        self.assertEqual(next_monday.weekday(), 0)
