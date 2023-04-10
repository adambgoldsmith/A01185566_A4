"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.battle import roll_critical_hit
from unittest.mock import patch


class TestRollCriticalHit(TestCase):
    @patch('random.randint', side_effect=[5])
    def test_roll_critical_hit_fail(self, _):
        self.assertEqual(False, roll_critical_hit())

    @patch('random.randint', side_effect=[2])
    def test_roll_critical_hit_success_two(self, _):
        self.assertEqual(True, roll_critical_hit())

    @patch('random.randint', side_effect=[1])
    def test_roll_critical_hit_success_one(self, _):
        self.assertEqual(True, roll_critical_hit())
