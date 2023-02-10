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
        self.bigrams = {}

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
        for i in range(len(words)):
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

        for i in range(len(words) - 1):
            bigram = words[i] + ' ' + words[i+1]
            if bigram not in self.bigrams:
                self.bigrams[bigram] = {}
            next_word = words[i+2] if i < len(words) - 2 else None
            if next_word not in self.bigrams[bigram]:
                self.bigrams[bigram][next_word] = 0
            self.bigrams[bigram][next_word] += 1



        
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

"""
Module for the Markov Chain
Responsible for generating sentences
"""
import random

class MarkovChain: # pylint: disable=R0903
    """
    The Markov Chain
    """
    def __init__(self, trie):
        self.trie = trie
        self.words_and_data = trie.getter(trie)
        self.words = list(self.words_and_data.keys())
        self.bigrams = trie.bigrams

    def generate_sentence(self, starting_word=None, max_length=7):
        """
        Generates max_length sentences starting from starting_word
        If no starting_word, chooses a random starting word
        """
        if starting_word is None:
            current_word = random.choice(self.words)
        else:
            current_word = starting_word
        sentence = current_word
        while len(sentence.split()) < max_length:
            next_words = self.trie.next_word(current_word)
            if next_words is None or not next_words:
                break
            next_word_frequencies = self.trie.next_word_frequencies(current_word)
            total_frequency = sum(next_word_frequencies.values())
            next_word = (random.choices(list(next_word_frequencies.keys()),
                weights=list(map(lambda x: x/total_frequency, next_word_frequencies.values())))[0])
            sentence += ' ' + next_word
            current_word = next_word
        return sentence.capitalize() + "."

    def generate_two_sentence(self):
        current_bigram = random.choice(list(self.bigrams.keys()))
        sentence = current_bigram.split()
        while current_bigram in self.bigrams:
            possibilities = self.bigrams[current_bigram]
            next_word = None
            if possibilities:
                next_word = random.choice(list(possibilities.keys()))
                if next_word is not None:
                    sentence.append(next_word)
            if next_word is None:
                break
            current_bigram = ' '.join(sentence[-2:])
        return ' '.join(sentence)



if __name__ == "__main__":
    t = Trie()
    t.insert("The cat is sleeping")
    t.insert("The cat is playing")
    t.insert("The dog is barking")
    mc = MarkovChain(t)
    print(mc.generate_two_sentence())
    