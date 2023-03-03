"""
Module for the Markov Chain
Responsible for generating sentences
"""
import random

class MarkovChain:
    """
    A class for generating sentences using a Markov Chain model.

    Attributes:
    - trie: An instance of a Trie data structure that represents the Markov Chain model.
    - words_and_data: A dictionary of all words and their data in the trie.
    - words: A list of all unique words in the Markov Chain model.
    - ngrams: A dictionary of all bigrams (pairs of consecutive words) in the Markov Chain model.
    """
    def __init__(self, trie):
        self.trie = trie
        self.words_and_data = trie.getter()
        self.words = list(self.words_and_data.keys())
        self.ngrams = trie.bigrams

    def generate_sentence(self, starting_word=None, max_length=50):
        """
        Generates a sentence using the Markov chain.

        Parameters:
        starting_word (str): the starting word for the sentence.
        If None, a random starting word will be chosen.
        max_length (int): the maximum length of the sentence.

        Returns:
        str: the generated sentence.
        """
        degree = len(list(self.ngrams.keys())[0].split())

        if starting_word in ("", None):
            current_ngram = random.choice(list(self.ngrams.keys()))
            sentence = str(current_ngram).split()

        else:
            values = self.handle_starting_prompt(starting_word, degree)
            current_ngram = values['current_ngram']
            sentence = values['sentence']

        while current_ngram in self.ngrams and len(sentence) < max_length:
            possibilities = self.ngrams[current_ngram]
            next_word = None
            if possibilities:
                next_word = random.choice(list(possibilities.keys()))

                if next_word is not None:
                    sentence.append(next_word)
            if next_word is None:
                break
            current_ngram = " ".join(sentence[-degree:])

        return " ".join(sentence).capitalize()

    def handle_starting_prompt(self, starting_word, degree):
        """
        Handles the starting prompt for the generated sentence.

        Parameters:
        starting_word (str): the starting word for the sentence.
        degree (int): the degree of the Markov chain.

        Returns:
        dict: a dictionary containing the current ngram and the sentence.
        """
        if len(starting_word.split()) >= degree:
            values = self.greater_or_equal_prompt(starting_word, degree)

        else:
            values = self.shorter_prompt(starting_word)

        current_ngram = values['current_ngram']
        sentence = values['sentence']
        return {"current_ngram":current_ngram, "sentence":sentence}

    def greater_or_equal_prompt(self, starting_word, degree):
        """
        Handles the starting prompt when the starting word contains
        at least as many words as the degree of the Markov chain.

        Parameters:
        starting_word (str): the starting word for the sentence.
        degree (int): the degree of the Markov chain.

        Returns:
        dict: a dictionary containing the current ngram and the sentence.
        """
        sentence = starting_word.split()
        current_ngram = " ".join(sentence[-degree:])
        return {"current_ngram":current_ngram, "sentence":sentence}


    def shorter_prompt(self, starting_word):
        """
        Handles the starting prompt when the starting word contains
        fewer words than the degree of the Markov chain.

        Parameters:
        starting_word (str): the starting word for the sentence.

        Returns:
        dict: a dictionary containing the current ngram and the sentence.
        """
        valid_ngrams = [ngram for ngram in self.ngrams.keys() if ngram.startswith(starting_word)]

        if len(valid_ngrams) > 0:
            current_ngram = random.choice(valid_ngrams)
            sentence = str(current_ngram).split()

        else:
            current_ngram = random.choice(list(self.ngrams.keys()))
            sentence = str(current_ngram).split()

        return {"current_ngram":current_ngram, "sentence":sentence}
