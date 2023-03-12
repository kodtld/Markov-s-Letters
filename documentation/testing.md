# Test Document

## Coverage
[![CI](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml/badge.svg)](https://github.com/kodtld/Markov-s-Letters/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)

## Tests
The tests cover the functionality of the trie_service and markov_service classes and their functions.<br><br>
The [coverage document](https://codecov.io/gh/kodtld/Markov-s-Letters) shows the test in detail. 

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
All operations need to be ran from flask-server directory, to navigate to the directory use command:
```
cd flask-server
```
### Unittests
To run the unittests, use command:
```
poetry run invoke test
```

### Pylint
To run pylint checks, use command:
```
poetry run invoke pylint
```

### Performance tests
To run the performance tests, use command:
```
poetry run invoke performance
```

### Performance of Trie_service

![Performance of trie_service](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/UPDATE_Trie_service_performance.jpg)

### Performance of Markov_service

#### One-state
![One-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/One_state_performance.jpg)

#### Two-state
![Two-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Two_state_performance.jpg)

#### Three-state
![Three-state performance](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Three_state_performance.jpg)
