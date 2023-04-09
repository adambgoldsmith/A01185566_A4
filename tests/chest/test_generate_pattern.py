"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from chest import generate_pattern
from unittest.mock import patch


class TestGeneratePattern(TestCase):
    @patch('random.choice', side_effect=['ruby', 'topaz', 'sapphire', 'topaz', 'emerald', 'ruby'])
    def test_generate_pattern_different_gems(self, _):
        self.assertEqual('IOVOXI', generate_pattern())

    @patch('random.choice', side_effect=['topaz', 'topaz', 'topaz', 'topaz', 'topaz', 'topaz'])
    def test_generate_pattern_all_topaz(self, _):
        self.assertEqual('OOOOOO', generate_pattern())

    @patch('random.choice', side_effect=['emerald', 'emerald', 'emerald', 'emerald', 'emerald', 'emerald'])
    def test_generate_pattern_all_emerald(self, _):
        self.assertEqual('XXXXXX', generate_pattern())

    @patch('random.choice', side_effect=['ruby', 'ruby', 'ruby', 'ruby', 'ruby', 'ruby'])
    def test_generate_pattern_all_ruby(self, _):
        self.assertEqual('IIIIII', generate_pattern())

    @patch('random.choice', side_effect=['sapphire', 'sapphire', 'sapphire', 'sapphire', 'sapphire', 'sapphire'])
    def test_generate_pattern_all_sapphire(self, _):
        self.assertEqual('VVVVVV', generate_pattern())
