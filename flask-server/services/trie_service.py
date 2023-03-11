"""
Includes the Trie (prefix-tree) for storing the words, its operations,
and TrieNode class for initializing the nodes
"""
import os
import string
import nltk # pylint: disable=W0611
from nltk.tokenize import PunktSentenceTokenizer

class TrieNode: # pylint: disable=R0903
    """
    Boilerplate for a node of the Trie
    Attributes:
    - children: A dictionary containing children nodes of the current node
    - is_sentence: A boolean indicating if the current node represents the end of a sentence
    - frequency: An integer representing the frequency of the current word in the Trie
    """
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.frequency = 0

class Trie:
    """
    The Trie (prefix-tree) for storing the words and generating ngrams
    Attributes:
    - root: A TrieNode object representing the root node of the Trie
    """
    def __init__(self):
        self.root = TrieNode()

    def insert_books(self): # pragma: no cover
        """
        Gets and inserts .txt format books into Trie from resources/books.
        Parameters: None
        Returns: None
        """
        banned_chars = string.digits + "●-;&_?!ãĩŃńōœũūǎǑǒǓǔǕǖǗǘǙǚǛǜɑṣṫṭṳṵṷṹṻỳỵỷỹ()”“‘" + '"'
        table = str.maketrans("", "", banned_chars)

        absolute_path = os.path.dirname(__file__)
        relative_path = "../resources/books"
        full_path = os.path.join(absolute_path, relative_path)
        directory = full_path
        for filename in os.listdir(directory):
            k = os.path.join(directory, filename)
            if os.path.isfile(k):
                with open(k,encoding='UTF-8',errors="ignore") as files: # pylint: disable=W1514
                    lines = files.read()
                    text = lines.translate(table)
                    tokenizer = PunktSentenceTokenizer()
                    for sentence in tokenizer.tokenize(text):
                        self.insert(sentence)

    def insert(self, sentence):
        """
        Inserts words from a sentence into the Trie.
        Parameters:
        - sentence: A string representing a sentence to be inserted into the Trie.
        Returns: None
        """
        words = sentence.upper().split()
        node = self.root
        for word in words:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_sentence = True
        node.frequency += 1

    def generate_ngrams(self, state):
        """
        Generates n-grams for the sentences stored in the Trie.

        Args:
            n (int): The size of the n-grams to generate.

        Returns:
            dict: A nested dictionary where the keys are n-grams (sequences of n words),
            and the values are dictionaries that map each follower word to its frequency.
            For example, the dictionary { "This is": { "rocket": 1, "league": 1 } }
            indicates that the n-gram (n == 2) "This is" appears in the text, and is followed
            by "rocket" and "league" with a frequency of 1 each.
        """
        ngrams = {}

        def dfs(node, prefix):
            if node.is_sentence:
                words = prefix.split()
                if len(words) >= state:
                    for i in range(len(words) - state + 1):
                        ngram = " ".join(words[i:i+state])
                        follower = words[i+state] if i+state < len(words) else None
                        if ngram not in ngrams:
                            ngrams[ngram] = {}
                        if follower not in ngrams[ngram]:
                            ngrams[ngram][follower] = 0
                        ngrams[ngram][follower] += 1
            for child_word, child_node in node.children.items():
                dfs(child_node, prefix + ' ' + child_word)

        dfs(self.root, '')

        return ngrams
