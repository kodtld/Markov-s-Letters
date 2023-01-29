import time
import nltk.data
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.is_sentence = False
        self.next_words = set()
        self.frequency = 0    

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert_books(self):
        directory = '/home/kxsalmi/markovs_letters/flask-server/resources/books'
        for filename in os.listdir(directory):
            k = os.path.join(directory, filename)
            if os.path.isfile(k):
                with open(k) as f:
                    lines = f.read()
                    text = lines
                    sentences = nltk.data.load('tokenizers/punkt/english.pickle')
                    for sentence in sentences.tokenize(text):
                            self.insert(sentence)
        
    def insert(self, sentence):
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

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word or current.is_sentence

    def next_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.next_words

    def frequency_of(self, word):
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
