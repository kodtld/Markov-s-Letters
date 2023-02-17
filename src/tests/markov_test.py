"""
Unittests for the Markov Chain
"""
import unittest
from services.trie_service import Trie
from services.markov_service import MarkovChain

class TestMarkovChain(unittest.TestCase):
    """
    Includes the tests for the Markov Chain
    """
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("On the other hand, we denounce with righteous indignation and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("Word is a bird")

    def test_generate_sentence(self):
        """
        Test if generate_sentence returns a valid sentence
        """
        markov_chain = MarkovChain(self.trie)
        result = markov_chain.generate_sentence(max_length=10)
        self.assertIsInstance(result, str)
        self.assertTrue(1 <= len(result.split()) <= 10)

    def test_generate_sentence_starting_word(self):
        """
        Test if generate_sentence starts with the specified starting word
        """
        markov_chain = MarkovChain(self.trie)
        result = markov_chain.generate_sentence(starting_word="word", max_length=10)
        self.assertTrue(result.startswith("Word"))

    def test_generate_two_sentence(self):
        """
        Test if generate_two_sentence returns a string of the expected length
        """
        markov_chain = MarkovChain(self.trie)
        result = markov_chain.generate_two_sentence(max_length=10)
        self.assertIsInstance(result, str)
        self.assertTrue(2 <= len(result.split()) <= 10)

if __name__ == '__main__':
    unittest.main()
