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
        self.assertTrue(self.trie.search("doing"))

    def test_search(self):
        """
        Tests the search of a word from the Trie
        """
        self.assertTrue(self.trie.search("doing"))
        self.assertFalse(self.trie.search("not_exist"))

    def test_frequency_of_word(self):
        """
        Tests the getting of a frequency of a word from the Trie
        """
        self.assertEqual(self.trie.frequency_of("cloud"), None)
        self.assertEqual(self.trie.frequency_of("world"), 1)
        self.assertEqual(self.trie.frequency_of("doing"), 2)

    def test_next_word(self):
        """
        Tests the getting of next possible words of a word from the Trie
        """
        self.assertEqual(self.trie.next_word("doing"), {'today', 'fine'})
        self.assertEqual(self.trie.next_word("not_exist"), None)

    def test_getter(self):
        """
        Tests the getter of every word and their frequency and followers
        """
        self.assertEqual(len(self.trie.getter(self.trie)), 16)

    def test_next_word_frequencies(self):
        """
        Tests the returns of possible following words and their frequencies
        """
        self.assertEqual(self.trie.next_word_frequencies("you"), {'doing': 2, 'say': 1})
        

if __name__ == '__main__':
    unittest.main()
