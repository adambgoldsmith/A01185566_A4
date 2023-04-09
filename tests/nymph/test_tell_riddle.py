"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from nymph import tell_riddle
from unittest.mock import patch


class TestTellRiddle(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tell_riddle(self, mock_output):
        riddle = ["What can you find at the end of a rainbow?",
                  "1. Absolutely nothing!", "2. A leprechaun's gold",
                  "3. The letter 'w'",
                  "4. A 7th colour",
                  '3']
        tell_riddle(riddle)
        tell_riddle_output = mock_output.getvalue()
        expected_output = "What can you find at the end of a rainbow?\n" \
                          "1. Absolutely nothing!\n" \
                          "2. A leprechaun's gold\n" \
                          "3. The letter 'w'\n" \
                          "4. A 7th colour\n"
        self.assertEqual(expected_output, tell_riddle_output)
