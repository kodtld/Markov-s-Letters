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

    def generate_sentence(self, starting_word=None, max_length=10):
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

    def generate_two_sentence(self, starting_word=None ,max_length=10):
        """
        Generates max_length two-state sentences starting from starting_bigram
        If no starting_bigram, chooses a random starting bigram
        """
        if starting_word in ("",None):
            current_bigram = random.choice(list(self.bigrams.keys()))
            sentence = current_bigram.split()

        elif starting_word not in ("",None):
            current_bigram = starting_word
            sentence = current_bigram.split()

        while current_bigram in self.bigrams and len(sentence) < max_length:
            possibilities = self.bigrams[current_bigram]
            next_word = None
            if possibilities:
                next_word = random.choice(list(possibilities.keys()))
                if next_word is not None:
                    sentence.append(next_word)
            if next_word is None:
                break
            current_bigram = ' '.join(sentence[-2:])
        return ' '.join(sentence).capitalize() + "."
