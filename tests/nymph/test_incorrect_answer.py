"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.nymph import incorrect_answer
from unittest.mock import patch


class TestIncorrectAnswer(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_answer_output_insufficient_gold(self, mock_output):
        character = {'inventory': {
            'gold': 0
        }}
        incorrect_answer(character)
        incorrect_answer_output = mock_output.getvalue()
        expected_output = "\"No no no!\" the nypmph groans.\n" \
                          "The nymph snaps it's fingers and a fresh fritzberry pie appears in their hand out of" \
                          " thin air.\n" \
                          "In a split second, the nymph splats the fritzberry pie directly into your face!\n" \
                          "The nymph sticks it's tongue out at you before flying away.\n" \
                          "You head back to your ship empty handed... And quite sticky...\n"
        self.assertEqual(expected_output, incorrect_answer_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_answer_output_sufficient_gold(self, mock_output):
        character = {'inventory': {
            'gold': 25
        }}
        incorrect_answer(character)
        incorrect_answer_output = mock_output.getvalue()
        expected_output = "\"No no no!\" the nypmph groans.\n" \
                          "The nymph snaps it's fingers and a fresh fritzberry pie appears in their hand out of" \
                          " thin air.\n" \
                          "In a split second, the nymph splats the fritzberry pie directly into your face!\n" \
                          "The nymph sticks it's tongue out at you before flying away.\n"\
                          "You check your pockets and notice 25 gold coins have been stolen.\n"\
                          "You head back to your ship empty handed... And quite sticky...\n"
        self.assertEqual(expected_output, incorrect_answer_output)

    def test_incorrect_answer_output_gold_stolen(self):
        character = {'inventory': {
            'gold': 25
        }}
        incorrect_answer(character)
        self.assertEqual(0, character['inventory']['gold'])

    def test_incorrect_answer_output_no_gold_stolen(self):
        character = {'inventory': {
            'gold': 24
        }}
        incorrect_answer(character)
        self.assertEqual(24, character['inventory']['gold'])
