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
        self.trie.insert("on the other hand, we denounce with righteous hate and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("that they cannot on the mat puke unfortunately")
        self.trie.insert("that they will see a cat in the mat")
        self.trie.insert("word is a bird")
        self.trie.insert("the cat in the hat sat on in a hat")
        self.markov_chain = MarkovChain(self.trie,2)
    
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
        result = self.markov_chain.generate_sentence(starting_word="word")
        print(result)
        self.assertTrue(result.startswith("Word"))
    
    def test_generate_sentence_break_if_no_next(self):
        """
        Test that generate_sentence doesn't start with a word not in the trie
        """
        result = self.markov_chain.generate_sentence(starting_word="suomi", max_length=10)
        self.assertNotEqual(result, "Suomi")

    def test_handle_starting_prompt_greater_or_equal(self):
        """
        Test the handling of a propmpt greater or equal in length to the degree
        """
        result = self.markov_chain.handle_starting_prompt("THE CAT IN", 2)
        self.assertEqual(result["current_ngram"], "CAT IN")
        self.assertEqual(result["sentence"], ["THE", "CAT", "IN"])

    def test_handle_starting_prompt_shorter(self):
        """
        Test the handling of a propmpt shorter in length to the degree
        """
        self.trie = Trie()
        self.trie.insert("On the other hand, we denounce with righteous hate and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("Word is a bird")
        self.trie.insert("The cat in the hat sat on in a hat")
        self.markov_chain = MarkovChain(self.trie,3)
        result = self.markov_chain.handle_starting_prompt("IN", 3)
        self.assertIn(result["sentence"][0], ["IN", "THE", "HAT", "MAT"])
    
    def test_handle_starting_prompt_shorter_no_found_matches(self):
        """
        Test the handling of a propmpt shorter in length to the degree with no matching Ngrams
        """
        self.trie = Trie()
        self.trie.insert("On the other hand, we denounce with righteous hate and dislike")
        self.trie.insert("that they cannot foresee the pain and trouble that are bound to")
        self.trie.insert("Word is a bird")
        self.trie.insert("The cat in the hat sat on in a hat")
        self.markov_chain = MarkovChain(self.trie,3)
        result = self.markov_chain.handle_starting_prompt("SUOMI", 3)
        self.assertIsInstance(result['sentence'][0], str)
        self.assertTrue(1 <= len(result["sentence"]) <= 10)

if __name__ == '__main__':
    unittest.main()
