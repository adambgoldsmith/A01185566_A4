"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from board import describe_current_location
from unittest.mock import patch


class TestDescribeCurrentLocation(TestCase):
    @patch('random.choice', side_effect=["There is only fog... As far as the eye can see..."])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output, _):
        region = [f"Fogmourne",
                  f"There is only fog... As far as the eye can see...",
                  f"You think you hear something slither through the dense fog, but you see nothing.",
                  f"The fog seems to have life to it; slowly crawling. Eerily silent.",
                  f"The haziness around you has a strange, sinister charm. Mysterious, yet melancholic."]
        describe_current_location(region)
        describe_current_location_output = mock_output.getvalue()
        expected_output = "There is only fog... As far as the eye can see...\n\n"
        self.assertEqual(expected_output, describe_current_location_output)
