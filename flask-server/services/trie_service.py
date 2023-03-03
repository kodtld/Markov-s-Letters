"""
Includes the Trie (prefix-tree) for storing the words, its operations,
and TrieNode class for initializing the nodes
"""
import os
import string
import nltk
from nltk.tokenize import PunktSentenceTokenizer

class TrieNode: # pylint: disable=R0903
    """
    Boilerplate for a node of the Trie
    Attributes:
    - children: A dictionary containing children nodes of the current node
    - is_word: A boolean indicating if the current node represents the end of a word
    - is_sentence: A boolean indicating if the current node represents the end of a sentence
    - next_words: A set containing the possible next words following the current node
    - frequency: An integer representing the frequency of the current word in the Trie
    """
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.is_sentence = False
        self.next_words = set()
        self.frequency = 0

class Trie:
    """
    The Trie (prefix-tree) for storing the words and its operations
    Attributes:
    - root: A TrieNode object representing the root node of the Trie
    - bigrams: A dictionary containing bigram frequency data for the Trie
    - ngram_length: An integer representing the length of N-grams to create from inserted sentences
    """
    def __init__(self, ngram_length = 2):
        self.root = TrieNode()
        self.bigrams = {}
        self.ngram_length = ngram_length

    def insert_books(self): # pragma: no cover
        """
        Gets and inserts .txt format books into Trie from resources/books.
        Parameters: None
        Returns: None
        """
        banned_chars = string.digits + "-;&_?!ãĩŃńōœũūǎǑǒǓǔǕǖǗǘǙǚǛǜɑṣṫṭṳṵṷṹṻỳỵỷỹ”“‘" + '"'
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
                    # sentences = nltk.data.load('tokenizers/punkt/english.pickle')
                    for sentence in tokenizer.tokenize(text):
                        print("-----------")
                        print(sentence)
                        print("-----------")
                        self.insert(sentence)

    def insert(self, sentence):
        """
        Inserts words from a sentence into the Trie, creating N-grams in the process.
        Parameters:
        - sentence: A string representing a sentence to be inserted into the Trie.
        Returns: None
        """
        n = self.ngram_length
        words = sentence.split()
        for i in range(len(words)): # pylint: disable=C0200
            current = self.root
            for char in words[i]:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.is_word = True

            if i < len(words) - 1:
                current.next_words.add(words[i+1])
            current.frequency += 1
        current.is_sentence = True

        for i in range(len(words) - n + 1):
            ngram = " ".join(words[i:i+n])
            if ngram not in self.bigrams:
                self.bigrams[ngram] = {}
            next_word = words[i+n] if i < len(words) - n else None
            if next_word not in self.bigrams[ngram]:
                self.bigrams[ngram][next_word] = 0
            self.bigrams[ngram][next_word] += 1

    def search(self, word):
        """
        Searches for a word in the Trie.
        Parameters:
        - word: A string representing the word to search for in the Trie.
        Returns:
        - True: If the word is found in the Trie.
        - False: If the word is not found in the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word or current.is_sentence

    def frequency_of(self, word):
        """
        Gets the frequency of a word in the Trie.
        Parameters:
        - word: A string representing the word to get the frequency of in the Trie.
        Returns:
        - An integer representing the frequency of the word in the Trie.
        - None: If the word is not found in the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.frequency

    def next_word(self, word):
        """
        Gets the possible next words following a given word in the Trie.
        Parameters:
        - word: A string representing the word to get the possible next words of in the Trie.
        Returns:
        - None: If the given word is not in the Trie.
        - A set containing the possible next words following the given word in the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.next_words

    def next_word_frequencies(self, word):
        """
        Returns a dictionary of possible next words for the given word and their
        frequencies in the Trie. If the given word is not found in the Trie,
        returns None.
        Parameters:
        word (str): The word for which to find the next word frequencies.
        Returns:
        dict: A dictionary mapping possible next words to their frequencies in the
            Trie, or None if the given word is not found in the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        next_word_frequencies = {}
        for next_word in current.next_words:
            next_word_frequencies[next_word] = self.frequency_of(next_word)
        return next_word_frequencies

    def getter(self):
        """
        Returns a dictionary containing information about each word in the Trie.
        Each key in the dictionary is a word in the Trie, and the value is a tuple
        containing the word, its frequency in the Trie, and a set of possible
        next words.
        Returns:
        dict: A dictionary containing information about each word in the Trie.
        """
        words_and_data = {}
        stack = [("", self.root)]
        while stack:
            word, node = stack.pop()
            if node.is_word or node.is_sentence:
                words_and_data[word] = (word ,node.frequency, node.next_words)
            for child_char, child_node in node.children.items():
                stack.append((word + child_char, child_node))
        return words_and_data