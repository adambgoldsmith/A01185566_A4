"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.chest import generate_puzzle
from unittest.mock import patch


class TestGeneratePuzzle(TestCase):
    @patch('chest.generate_pattern', side_effect=['XOXIIV'])
    @patch('random.randint', side_effect=[3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_puzzle_pattern_output(self, mock_output, _, __):
        generate_puzzle()
        generate_puzzle_output = mock_output.getvalue()
        expected_output = "XOXIIVXOX\n"
        self.assertEqual(expected_output, generate_puzzle_output)

    @patch('chest.generate_pattern', side_effect=['XVOIVX'])
    @patch('random.randint', side_effect=[3])
    def test_generate_puzzle_random_pattern(self, _, __):
        self.assertEqual("I", generate_puzzle())

    @patch('chest.generate_pattern', side_effect=['VVVVVV'])
    @patch('random.randint', side_effect=[5])
    def test_generate_puzzle_all_same(self, _, __):
        self.assertEqual("V", generate_puzzle())
