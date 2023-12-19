import unittest
from hangman import get_word

class TestGetWordFunction(unittest.TestCase):
    
    def test_non_empty_word(self):
        # Test to ensure the get_word function returns a non-empty string
        word = get_word()
        self.assertTrue(isinstance(word, str))
        self.assertTrue(len(word) > 0)

    def test_different_words_on_consecutive_calls(self):
        # Test to ensure the get_word function returns different words on consecutive calls
        word1 = get_word()
        word2 = get_word()
        self.assertNotEqual(word1, word2)

if __name__ == '__main__':
    unittest.main()

# use python -m unittest test_get_word.py to test