import io
from unittest import TestCase
from shop import sufficient_gold
from unittest.mock import patch


class TestSufficientGold(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sufficient_gold_sufficient_output(self, mock_output):
        character = {'inventory': {
            'gold': 100
        }}
        sufficient_gold(character)
        sufficient_gold_output = mock_output.getvalue()

        self.fail()
