from src.utils import next_day_of_week, determine_number_suffix

from datetime import datetime
import unittest


class TestUtils(unittest.TestCase):

    def test_next_day_of_week(self):
        now = datetime.now()
        next_monday = next_day_of_week(0, now)
        print(next_monday)
        self.assertEqual(next_monday.weekday(), 0)

    def test_determine_number_suffix(self):
        numbers = [
            {"value": 1, "expected": "st"},
            {"value": 2, "expected": "nd"},
            {"value": 3, "expected": "rd"},
            {"value": 4, "expected": "th"},
            {"value": 323, "expected": "rd"},
            {"value": 101, "expected": "st"},
            {"value": 452, "expected": "nd"}
        ]
        for number in numbers:
            test_value = number.get('value')
            expected = number.get('expected')
            actual = determine_number_suffix(test_value)
            self.assertEqual(actual, expected)
