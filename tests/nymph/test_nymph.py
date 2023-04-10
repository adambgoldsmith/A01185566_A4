"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.nymph import nymph
from unittest.mock import patch


class TestNymph(TestCase):
    @patch('helper_functions.nymph.generate_riddle', side_effect=[['t', 'e', 's', 't', 's', '!']])
    @patch('helper_functions.nymph.tell_riddle', side_effect=[None])
    @patch('helper_functions.nymph.user_riddle_choice', side_effect=['1'])
    @patch('helper_functions.nymph.correct_answer', side_effect=[None])
    @patch('helper_functions.nymph.incorrect_answer', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nymph(self, mock_output, _, __, ___, ____, ______):
        character = {'inventory': {
            'gold': 0
        }}
        nymph(character)
        nymph_output = mock_output.getvalue()
        expected_output = "\n-------------------------\n" \
                          "You notice a small sky-island as you drift through the air.\n" \
                          "You dock your ship and cross over to the island.\n" \
                          "A small cloud nymph is standing beneath some trees, dancing and singing.\n" \
                          "The nymph approaches playfully and chants to you:\n" \
                          "\"Solve my riddle and rewarded thee shall be! Falter in riposte and a trick you will see!\"\n\n"
        self.assertEqual(expected_output, nymph_output)

    def test_nymph_type_error(self):
        with self.assertRaises(TypeError):
            nymph(None)
