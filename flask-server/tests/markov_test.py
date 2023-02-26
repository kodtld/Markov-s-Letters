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
        self.trie = Trie(1)
        self.trie.insert("On the other hand, we denounce with righteous hate and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("that they cannot on the mat puke unfortunately")
        self.trie.insert("that they will see a cat in the mat")
        self.trie.insert("Word is a bird")
        self.trie.insert("The cat in the hat sat on in a hat")
        self.markov_chain = MarkovChain(self.trie)
    def test_generate_sentence(self):
        """
        Test if generate_sentence returns a valid sentence
        """
        result = self.markov_chain.generate_sentence(max_length=10)
        self.assertIsInstance(result, str)
        self.assertTrue(1 <= len(result.split()) <= 10)

    def test_generate_sentence_starting_word(self):
        """
        Test if generate_sentence starts with the specified starting word
        """
        result = self.markov_chain.generate_sentence(starting_word="word", max_length=10)
        print(result)
        self.assertTrue(result.startswith("Word"))

    def test_generate_two_sentence_no_bigram(self):
        """
        Test if generate_two_sentence with no starting bigram returns a string of the expected length
        """
        result = self.markov_chain.generate_sentence(max_length=10)
        self.assertIsInstance(result, str)
        self.assertTrue(2 <= len(result.split()) <= 10)

    def test_generate_two_sentence_set_bigram(self):
        """
        Test if generate_two_sentence with a starting bigram returns a string of the expected length
        """
        result = self.markov_chain.generate_sentence(starting_word="that they",max_length=10)
        self.assertIsInstance(result, str)
        self.assertTrue(2 <= len(result.split()) <= 10)
    
    def test_handle_starting_prompt_greater_or_equal(self):
        """
        Test the handling of a propmpt greater or equal in length to the degree
        """
        result = self.markov_chain.handle_starting_prompt("the cat in", 2)
        self.assertEqual(result["current_ngram"], "cat in")
        self.assertEqual(result["sentence"], ["the", "cat", "in"])

    def test_handle_starting_prompt_shorter(self):
        """
        Test the handling of a propmpt shorter in length to the degree
        """
        self.trie = Trie(3)
        self.trie.insert("On the other hand, we denounce with righteous hate and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("Word is a bird")
        self.trie.insert("The cat in the hat sat on in a hat")
        self.markov_chain = MarkovChain(self.trie)
        result = self.markov_chain.handle_starting_prompt("in", 2)
        self.assertIn(result["sentence"][0], ["in", "the", "hat", "mat"])

if __name__ == '__main__':
    unittest.main()
