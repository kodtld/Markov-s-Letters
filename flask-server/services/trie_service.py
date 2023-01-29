"""
Includes the Trie (prefix-tree) for storing the words, its operations,
and TrieNode class for initializing the nodes
"""
import os
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
        directory = 'resources/books'
        for filename in os.listdir(directory):
            k = os.path.join(directory, filename)
            if os.path.isfile(k):
                with open(k) as files: # pylint: disable=W1514
                    lines = files.read()
                    text = lines
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

# if __name__ == "__main__":
#     t = Trie()
#     print(t.search("world"))
#     print(t.search("doing"))
#     print(t.next_word("doing"))
#     print(t.frequency_of("doing"))
#     print(t.next_words_for_sentence("doing"))
