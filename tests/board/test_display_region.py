"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.board import display_region
from unittest.mock import patch


class TestDisplayRegion(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_region(self, mock_output):
        region = [f"The Cloud Expanse",
                  f"The several thousand clouds here mesmerize you",
                  f"The sun reflects off of the glittering clouds that surround you.",
                  f"A flock of seagulls fly overhead, squawking loudly.",
                  f"The blue sky is dotted with fluffy white clouds. The view is breathtaking."]
        display_region(region)
        display_region_output = mock_output.getvalue()
        expected_output = "-------------------------\n" \
                          "The Cloud Expanse\n"
        self.assertEqual(expected_output, display_region_output)
