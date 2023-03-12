# Markov's Sentences
[![CI](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml/badge.svg)](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)
![Markov UI](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_UI.png)

## Installation
You can download the project with the command:
```
git clone https://github.com/kodtld/Markov-s-Letters
```
## Running
Running of the program doesn't require installation of *Python* or *Poetry*, but both are necessary to run the [tests.](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/testing.md) <br><br>

**All commands are to be ran from the *flask-server* directory**, to which you can navigate with the command:
```
cd flask-server
```
If your system doesn't have *Poetry* installed, you can run the application with following commands:
```
cd dist
```
```
./server
```
If you have *Poetry* installed, you can run the application from the flask-server directory with:
```
poetry run invoke start
```
**In either case, once the application is running, you need to manually open localhost:5000 in a browser of your choosing.**

## General Information
The program begins by reading text from books and tokenizing them into individual words. It then inserts these words into a trie data structure, which allows for efficient storage and retrieval of words.<br> The trie is then used to generate n-grams of length n, which are subsequences of n words that appear together in the text. The Ngrams contain the Ngram itself, it's possible followers, and for each follower, it's frequency in the Trie.<br><br>
![Trie_1](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/trie_info_1.png)
*Displayed above is the general structure of a trie. Unlike in the image, my Trie has full words as nodes instead of letters.*
<br><br>
These n-grams are then passed to a Markov chain class, which uses them to generate sentences. A Markov chain is a probabilistic model that predicts the next word in a sequence based on the previous words. By using the n-grams generated from the trie, the Markov chain can generate sentences that are similar in style and content to the original text.
![Markov GIF](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_info.gif)
*The Markov Chain gets the weight of possible followers from the Ngrams*

## Documentation
[User Manual](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/manual.md) <br><br>
[Test Document](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/testing.md) <br><br>
[Specification Document](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/specification.md) <br><br>
[Implementation Document](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/implementation.md) <br><br>
[General Information](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/info.md)

## Weekly reports
### Week 1
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_1.md)
### Week 2
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_2.md)
### Week 3
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_3.md)
### Week 4
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_4.md)
### Week 5
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_5.md)
### Week 6
[Report](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/weekly_reports/Week_6.md)
