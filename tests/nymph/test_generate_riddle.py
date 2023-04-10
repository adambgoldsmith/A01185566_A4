"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.nymph import generate_riddle
from unittest.mock import patch


class TestGenerateRiddle(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_generate_riddle(self, _):
        riddle = ["What can you find at the end of a rainbow?",
                  "1. Absolutely nothing!",
                  "2. A leprechaun's gold",
                  "3. The letter 'w'",
                  "4. A 7th colour",
                  '3']
        self.assertEqual(riddle, generate_riddle())
