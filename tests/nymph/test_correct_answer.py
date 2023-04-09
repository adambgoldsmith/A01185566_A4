import io
from unittest import TestCase
from nymph import correct_answer
from unittest.mock import patch


class TestCorrectAnswer(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_answer_output(self, mock_output):
        character = {'inventory': {
            'gold': 10
        }}
        correct_answer(character)
        correct_answer_output = mock_output.getvalue()
        expected_output = "\"CORRECT!\" the nymph giggles.\n" \
                          "\"A promise is a promise!\"\n" \
                          "The nymph hands you a small leather pouch filled with 50 gold coins!\n" \
                          "You head back to your ship with a grin.\n"
        self.assertEqual(expected_output, correct_answer_output)

    def test_correct_answer_gold_added(self):
        character = {'inventory': {
            'gold': 10
        }}
        correct_answer(character)
        self.assertEqual(60, character['inventory']['gold'])
