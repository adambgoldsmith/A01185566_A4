import io
from unittest import TestCase
from character import display_stats
from unittest.mock import patch


class TestDisplayStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_stats(self, mock_output):
        character = {
            'level': 1,
            'experience': 0,
            'max_health': 100,
            'health': 100,
        }
        display_stats(character)
        display_stats_output = mock_output.getvalue()
        expected_output = "HP: 100/100 |~| XP: 0/100 |~| Lvl: 1\n\n"
        self.assertEqual(expected_output, display_stats_output)
