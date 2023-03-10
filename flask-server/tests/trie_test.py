"""
Unittests for the Trie
"""
import unittest
from services.trie_service import Trie,TrieNode

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        
    def test_insert_single_word(self):
        self.trie.insert('hello')
        node = self.trie.root.children['HELLO']
        self.assertIsInstance(node, TrieNode)
        self.assertEqual(node.is_sentence, True)
        self.assertEqual(node.frequency, 1)
        self.assertEqual(len(self.trie.root.children), 1)
        
    def test_insert_multiple_words(self):
        self.trie.insert('hello world')
        node_hello = self.trie.root.children['HELLO']
        node_world = node_hello.children['WORLD']
        self.assertIsInstance(node_hello, TrieNode)
        self.assertIsInstance(node_world, TrieNode)
        self.assertEqual(node_hello.is_sentence, False)
        self.assertEqual(node_world.is_sentence, True)
        self.assertEqual(len(self.trie.root.children), 1)
        self.assertEqual(len(node_hello.children), 1)
        
    def test_insert_same_word_multiple_times(self):
        self.trie.insert('hello')
        self.trie.insert('hello')
        node = self.trie.root.children['HELLO']
        self.assertEqual(node.frequency, 2)
        
    def test_generate_ngrams_single_sentence(self):
        self.trie.insert('hello world')
        ngrams = self.trie.generate_ngrams(2)
        expected = {'HELLO WORLD': {None: 1}}
        self.assertEqual(ngrams, expected)
        
    def test_generate_ngrams_multiple_sentences(self):
        self.trie.insert('hello world')
        self.trie.insert('hello world')
        self.trie.insert('world hello')
        ngrams = self.trie.generate_ngrams(2)
        expected = {'HELLO WORLD': {None: 1}, 'WORLD HELLO': {None: 1}}
        self.assertEqual(ngrams, expected)
        
    def test_generate_ngrams_no_matches(self):
        self.trie.insert('hello world')
        ngrams = self.trie.generate_ngrams(3)
        expected = {}
        self.assertEqual(ngrams, expected)
        
if __name__ == '__main__':
    unittest.main()

