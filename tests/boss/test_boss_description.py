"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.boss import boss_description
from unittest.mock import patch


class TestBossDescription(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_description_output(self, mock_output):
        boss = {'name': 'Nebulous, The Mist Colossus'}
        region = ['Fogmourne']
        boss_description(boss, region)
        boss_description_output = mock_output.getvalue()
        expected_output = "As you near the far reaches of Fogmourne you sense the presence of an immense darkness.\n" \
                          "From beneath the clouds, Nebulous, The Mist Colossus, swoops into" \
                          " view and blocks your path.\n" \
                          "You prepare for a tough battle...\n"
        self.assertEqual(expected_output, boss_description_output)
