# Markov's Letters
### | TKT | Python | English |
## General
I am writing a program in Python that aims to generate sentences, either with no input, or using a user inputted word as the first word of the sentence.

My goal is to initialize a trie with text from novels, and generating sentences using either a Markov chain based on the user's current input, or no input. The user's input is given in a text field and the program provides generated sentences using the input as the first word of the sentence. On top of the text, the user can choose how many steps should be taken into consideration (one-step markov, two-step markov, ...).

I chose the topic because it seemed like a proper challenge, but a manageable one. I believe it'll be a fitting project for my first poke at machine learning.

## Expected time and space complexities
The time complexity for inserting a word into a trie is O(n), where n is the length of the word. The time complexity for searching for a word in a trie is also O(n), where n is the length of the word being searched for. The space complexity for a trie is O(m * n), where m is the number of words in the trie and n is the average length of a word in the trie.

The time complexity for generating the Markov chain model from the trie data structure should be O(m * n), where m is the number of words in the trie and n is the average length of a word in the trie. Once the Markov chain model is generated, I think the time complexity for using it to get the next word in a sentence should be around O(1) on average, assuming that the previous words in the sentence are used as the state of the Markov chain.

The space complexity for storing the Markov chain model will depend on the number of states and transitions in the model. It should be O(w * s), where w is the number of words in the trie and s is the number of states in the Markov chain model.

## Sources/Links
[Implementing Trie in Python by Albert Au Yeung](https://albertauyeung.github.io/2020/06/15/python-trie.html/) <br><br>
[From “What is a Markov Model” to “Here is how Markov Models Work” by Alexander Dejeu](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)<br><br>
[Text Generation with Markov Chains: An Introduction to using Markovify by Gregory Pernicano](https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33)<br><br>
[Trie: An Efficient Data Structure for String Processing](https://www.enjoyalgorithms.com/blog/introduction-to-trie-data-structure)<br><br>
[DFS vs BFS (in detail)](https://iq.opengenus.org/dfs-vs-bfs/)<br><br>
