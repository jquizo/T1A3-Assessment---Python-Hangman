import unittest
from hangman import get_word

class TestGetWordFunction(unittest.TestCase):
    
    def test_non_empty_word(self):
        # Test to ensure the get_word function returns a non-empty string
        word = get_word()
        self.assertTrue(isinstance(word, str))
        self.assertTrue(len(word) > 0)

if __name__ == '__main__':
    unittest.main()

# use python -m unittest test_get_word.py to test