"""
Includes the Trie (prefix-tree) for storing the words, its operations,
and TrieNode class for initializing the nodes
"""
import os
import string
import nltk.data

class TrieNode: # pylint: disable=R0903
    """
    Boilerplate for a node of the Trie
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
    """
    def __init__(self):
        self.root = TrieNode()

    def insert_books(self): # pragma: no cover
        """
        Gets and inserts (self.insert) .txt format books into Trie from resources/books
        """
        banned_chars = string.punctuation + string.digits + ":;()/$'!?“”'‘’-"
        table = str.maketrans("", "", banned_chars)

        absolute_path = os.path.dirname(__file__)
        relative_path = "../resources/books"
        full_path = os.path.join(absolute_path, relative_path)
        directory = full_path
        for filename in os.listdir(directory):
            k = os.path.join(directory, filename)
            if os.path.isfile(k):
                with open(k) as files: # pylint: disable=W1514
                    lines = files.read()
                    text = lines.translate(table)
                    sentences = nltk.data.load('tokenizers/punkt/english.pickle')
                    for sentence in sentences.tokenize(text):
                        self.insert(sentence)


    def insert(self, sentence):
        """
        Inserts sentences word by word into Trie
        """
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

    def search(self, word):
        """
        Searches if a word is present in the Trie
        Returns True or False
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word or current.is_sentence

    def getter(self,trie):
        """
        Returns every word, their possible followers, and their frequency
        Can be searched for a specific word by calling: getter(trie)['word']
        """
        words_and_data = {}
        stack = [("", trie.root)]
        while stack:
            word, node = stack.pop()
            if node.is_word or node.is_sentence:
                words_and_data[word] = (word ,node.frequency, node.next_words)
            for child_char, child_node in node.children.items():
                stack.append((word + child_char, child_node))
        return words_and_data

    def next_word(self, word):
        """
        Searches for the next possible words of given word
        Returns None or dictionary of words
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.next_words

    def frequency_of(self, word):
        """
        Returns how many times a word is present in the Trie
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.frequency

    def next_word_frequencies(self, word):
        """
        Returns possible words after parameter word and their frequencies
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
