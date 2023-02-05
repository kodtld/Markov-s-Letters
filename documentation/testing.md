# Testing document

## Coverage
[![codecov](https://codecov.io/gh/kodtld/Markov-s-Letters/branch/master/graph/badge.svg?token=GZHXEZIJ17)](https://codecov.io/gh/kodtld/Markov-s-Letters)

## Tests
The tests cover the functionality of the trie_service class and its functions.
There's a test for every function with valid and invalid values, for example, returning frequencies of all words in the trie or searching for followers of a nonexistent word returning None. The coverage document linked above shows all of the tests. 

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
