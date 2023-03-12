# Test Document

## Coverage
[![CI](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml/badge.svg)](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)

## Tests
The tests cover the functionality of the trie_service and markov_service classes and their functions.
The coverage document linked above shows all of the tests. 

## Trie

### Basic functionality
The basic functionalities tested are as follows:
- Manually inserted words are present in the trie.
- Searching for a word present returns True.
  - Inserting same word twice raises frequency.

### Advanced functionality
The more advance functionalities tested are as follows:
- Generation of Ngrams is tested with a Trie containing one or multiple sentences.
  - Also tested negative return in case there's not enough data to generate N state Ngrams.

### Performance
There's also performance tests for the operations of the trie such as:
- Inserting the books into the trie.
- Generating Ngrams with different degrees.

## Markov
### Basic functionality
The basic functionalities tested are as follows:
- Testing that generating a sentence returns a valid sentence with no starting prompt.
- Testing that generating a sentence returns a valid sentence with a given starting prompt.
- Testing the handling of the starting prompt(shorter, equal, or greater(in length compared to degree of Markov))

### Performance
There's also performance tests for the generation of sentences:
- Generating sentences with state == 1.
- Generating sentences with state == 2.
- Generating sentences with state == 3.

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
