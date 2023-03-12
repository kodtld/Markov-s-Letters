# General Information
The program begins by reading text from books and tokenizing them into individual words. It then inserts these words into a trie data structure, which allows for efficient storage and retrieval of words.<br> The trie is then used to generate n-grams of length n, which are subsequences of n words that appear together in the text. The Ngrams contain the Ngram itself, it's possible followers, and for each follower, it's frequency in the Trie.<br><br>
![Trie_1](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/trie_info_1.png)
*Displayed above is the general structure of a trie. Unlike in the image, my Trie has full words as nodes instead of letters.*
<br><br>
These n-grams are then passed to a Markov chain class, which uses them to generate sentences. A Markov chain is a probabilistic model that predicts the next word in a sequence based on the previous words. By using the n-grams generated from the trie, the Markov chain can generate sentences that are similar in style and content to the original text.
![Markov GIF](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_info.gif)
*The Markov Chain gets the weight of possible followers from the Ngrams*
