"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from character import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_true(self):
        character = {'health': 50}
        self.assertEqual(True, is_alive(character))

    def test_is_alive_false_zero(self):
        character = {'health': 0}
        self.assertEqual(False, is_alive(character))

    def test_is_alive_false_negative(self):
        character = {'health': -50}
        self.assertEqual(False, is_alive(character))
