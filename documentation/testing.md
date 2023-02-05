# Testing document

## Coverage
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)

## Tests
The tests cover the functionality of the trie_service class and its functions.
The coverage document linked above shows all of the tests. 

### Basic functionality
The basic functionalities tested are as follows:
- Manually inserted words are present in the trie
- Searching for a word present returns True
-- A nonexistent word returns None

### Advanced functionality
The more advance functionalities tested are as follows:
- Frequency search of a word in the trie returns its frequency
  - A nonexistent word returns None
- Next words search for a word in the trie returns a dictionary of the words that appear after the word
  - A nonexistent word returns None
- Next words & frequencies search for a word in the trie returns a dictionary of the words that appear after the word and their frequencies
  - A nonexistent word returns None
- The getter returns every word and their frequency and followers

## Run tests
To run the test you need to be in the flask-server repository.
You can access the flask-server repository from the root folder with:
```
cd flask-server
```
When in flask-server repo. you can run the tests with the following command:
```
coverage run -m pytest tests
```
After running the tests, you can generate the coverage report with:
```
coverage report -m

```
