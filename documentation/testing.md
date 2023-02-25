# Test Document

## Coverage
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)

## Tests
The tests cover the functionality of the trie_service and markov_service classes and their functions.
The coverage document linked above shows all of the tests. 

## Trie

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

### Performance
At the moment there's performance tests for the basic functionality of the trie such as:
- Inserting the books into the trie
- Searching for a specific word in the trie
- Searching for the frequency of a specific word
- Searching for the followers of a specific word
- Searching for the frequencies of following words

## Markov
### Basic functionality
The basic functionalities tested are as follows:
- Testing that generating a one-state sentence returns a sentence of valid length
- Testing that generating a one-state sentence with given starting word generates a valid sentence
- Testing that generating a two-state sentence returns a sentence of valid length

## Run tests
### Unittests
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
## Performance tests
### Trie_service

You can run the performance test/report for the trie_service from the flask-server directory with the following command:
```
python3 performance_trie.py
```
![Performance of trie_service](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/UPDATE_Trie_service_performance.jpg)

### Markov_service

You can run the performance test/report for the markov_service from the flask-server directory with the following command:
```
python3 performance_markov.py
```
#### One-state
![One-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/One_state_performance.jpg)

#### Two-state
![Two-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Two_state_performance.jpg)

#### Three-state
![Three-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Three_state_performance.jpg)
