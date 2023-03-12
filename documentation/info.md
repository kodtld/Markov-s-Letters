# General Information
The program begins by reading text from books and tokenizing them into individual words. It then inserts these words into a trie data structure, which allows for efficient storage and retrieval of words.<br> The trie is then used to generate n-grams of length n, which are subsequences of n words that appear together in the text. The Ngrams contain the Ngram itself, it's possible followers, and for each follower, it's frequency in the Trie.<br><br>
![Trie_1](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/trie_info_1.png)
*Displayed above is the general structure of a trie. Unlike in the image, my Trie has full words as nodes instead of letters.*


## Markov Chain
### Basic Idea
![Markov 1](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_info1.jpeg)
### Weigth
![Markov 2](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_info2.jpeg)
### Generation
![Markov GIF](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_info.gif)
### Source
[From “What is a Markov Model” to “Here is how Markov Models Work” by Alexander Dejeu](https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71)
