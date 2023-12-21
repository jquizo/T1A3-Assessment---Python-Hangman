import unittest
from unittest.mock import patch
from io import StringIO
from hangman import play

class TestPlayFunction(unittest.TestCase):
    # Test when no more tries are left
    def test_play_no_tries_left(self):
        
        # Simulates user input (to trigger running out of tries)
        with patch("builtins.input", side_effect=["O", "Y", "M", "A", "B", "C"]):
            # Run the play() function with the word "TEST"
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                play("TEST")
                output = mock_stdout.getvalue().strip()

        expected_output = "Sorry, you ran out of tries. The word was TEST. Better luck next time! Score: 0"
        self.assertIn(expected_output, output)
    
if __name__ == "__main__":
    unittest.main()

# use python -m unittest test_play_function.py on terminal to test