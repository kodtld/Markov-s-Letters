"""
Unittests for the Trie
"""
import unittest
from services.trie_service import Trie

class TestTrie(unittest.TestCase):
    """
    Includes the tests for the Trie
    """
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("Hello world how are you doing today")
        self.trie.insert("I am doing fine thank you")
        self.trie.insert("What did you say my friend")

    # def test_insert_books(self):
    #     """
    #     Tests the insert of books from resources/books
    #     """
    #     self.trie.insert_books()
    #     self.assertEqual(len(self.trie.root.children), 91)

    def test_insert(self):
        """
        Tests the insert of a sentence
        """
        self.assertTrue(self.trie.search("world"))

    def test_search_valid(self):
        """
        Tests the search of a word from the Trie
        """
        self.assertTrue(self.trie.search("doing"))

    def test_search_invalid(self):
        """
        Tests the search of an invalid word from the Trie
        """
        self.assertFalse(self.trie.search("football"))

    def test_frequency_of_invalid_word(self):
        """
        Tests the getting of a frequency of an invalid word from the Trie
        """
        self.assertEqual(self.trie.frequency_of("cloud"), None)

    def test_frequency_of_one_word(self):
        """
        Tests the getting of a frequency of a word appearing once from the Trie
        """
        self.assertEqual(self.trie.frequency_of("world"), 1)

    def test_frequency_of_two_word(self):
        """
        Tests the getting of a frequency of a word appearing twice from the Trie
        """
        self.assertEqual(self.trie.frequency_of("doing"), 2)

    def test_next_word_valid(self):
        """
        Tests the getting of next possible words of a word from the Trie
        """
        self.assertEqual(self.trie.next_word("doing"), {'today', 'fine'})

    def test_next_word_invalid(self):
        """
        Tests the getting of next possible words of an invalid word from the Trie
        """
        self.assertEqual(self.trie.next_word("football"), None)

    def test_getter(self):
        """
        Tests the getter of every word and their frequency and followers
        """
        self.assertEqual(len(self.trie.getter(self.trie)), 16)

    def test_next_word_frequencies_valid(self):
        """
        Tests the return of possible following words and their frequencies for a word
        """
        self.assertEqual(self.trie.next_word_frequencies("you"), {'doing': 2, 'say': 1})

    def test_next_word_frequencies_invalid(self):
        """
        Tests the return of possible following words and their frequencies for an invalid word
        """
        self.assertEqual(self.trie.next_word_frequencies("football"), None)

if __name__ == '__main__':
    unittest.main()
