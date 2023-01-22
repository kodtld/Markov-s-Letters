# Markov's Letters
### | TKT | Python | English |
## General
I am writing a program in Python that aims to predict the word the user is typing based on the letters provided. My goal is to initialize a trie tree with 58,000 English words and to make real-time predictions using a Markov chain based on the user's current input. The user's input is given in a text field and the program provides the four most relevant predictions based on the current state of the input. I chose the topic because it seemed like a proper challenge, but a manageable one. I believe it'll be a fitting project for my first poke at machine learning.

## Time and space
The time complexity for inserting a word into a trie is O(n), where n is the length of the word. The time complexity for searching for a word in a trie is also O(n), where n is the length of the word being searched for. The space complexity for a trie is O(m * n), where m is the number of words in the trie and n is the average length of a word in the trie.

The time complexity for generating the Markov chain model from the trie data structure should be O(m * n), where m is the number of words in the trie and n is the average length of a word in the trie. Once the Markov chain model is generated, I think the time complexity for using it to predict the next word in a sentence should be around O(1) on average, assuming that the previous words in the sentence are used as the state of the Markov chain.

The space complexity for storing the Markov chain model will depend on the number of states and transitions in the model. It should be O(w * s), where w is the number of words in the trie and s is the number of states in the Markov chain model.

## Sources
Added later...
