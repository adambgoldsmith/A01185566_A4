"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.board import display_board
from unittest.mock import patch


class TestDisplayBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_non_square(self, mock_output):
        rows = 5
        columns = 6
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        display_board(rows, columns, character)
        display_board_output = mock_output.getvalue()
        expected_output = "o/ [] [] [] [] []\n"\
                          "[] [] [] [] [] []\n" \
                          "[] [] [] [] [] []\n" \
                          "[] [] [] [] [] []\n" \
                          "[] [] [] [] [] []\n"
        self.assertEqual(expected_output, display_board_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_smallest(self, mock_output):
        rows = 5
        columns = 5
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        display_board(rows, columns, character)
        display_board_output = mock_output.getvalue()
        expected_output = "o/ [] [] [] []\n" \
                          "[] [] [] [] []\n" \
                          "[] [] [] [] []\n" \
                          "[] [] [] [] []\n" \
                          "[] [] [] [] []\n"
        self.assertEqual(expected_output, display_board_output)
