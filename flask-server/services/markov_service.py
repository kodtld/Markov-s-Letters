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
