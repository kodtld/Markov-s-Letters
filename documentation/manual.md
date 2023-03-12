# User Manual
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
If your system doesn't have *Poetry* installed, you can run the application with following steps:
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
## Tests
**All testing operations need to be ran from *flask-server* directory and require the installation of *Python* and *Poetry***, to navigate to the directory use command:
```
cd flask-server
```
### Unittests
To run the unittests, use command:
```
poetry run invoke test
```

### Pylint
Pylint check includes files:
- server.py
- trie_service.py
- markov_service.py <br>

To run pylint checks, use command:
```
poetry run invoke pylint
```

### Performance tests
To run the performance tests, use command:
```
poetry run invoke performance
```
