import io
from unittest import TestCase
from nymph import nymph
from unittest.mock import patch


class TestNymph(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nymph(self, mock_output):
        character = {'inventory': {
            'gold': 0
        }}
        nymph(character)
        nymph_output = mock_output.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, nymph_output)
