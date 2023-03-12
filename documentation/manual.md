# User Manual
## Usage
![Markov UI](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/images/Markov_UI.png)
The usage of the application is pretty straightforward.<br><br>
Use the slider to select the state/degree of Markov in which the generation of sentences should happen in. The states available are 1-5 and the output differs depending on selected state.<br><br>
- Degree 1: A Markov chain of degree 1 only considers the current state and its immediate successor.
- Degree 2: A Markov chain of degree 2 considers the current state, its immediate successor, and the state that precedes the current state.
- Degree 3: A Markov chain of degree 3 considers the current state, its immediate successor, the state that precedes the current state, and the state that precedes the predecessor of the current state.
- Degree 4: A Markov chain of degree 4 considers the current state, its immediate successor, the two states that precede the current state, and the state that precedes the predecessor of the current state.
- Degree 5: A Markov chain of degree 5 considers the current state, its immediate successor, the two states that precede the current state, and the two states that precede the predecessor of the current state.<br>

If you just select the state and hit generate, the application will generate corresponding degree sentences based on the corpus. <br><br>
You can also give a starting prompt (not case sensitive), and if the given word/sequence is found in the corpus, the generation will start with given prompt. If the prompt is shorter than selected state (ex. one word prompt with state 2) and it's not found in the corpus, the generator will select a random starting Ngram for the generation. The corpus is stripped of numerals, so if a numeral is given as starting prompt, a random Ngram is selected.              
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
## Further development
If the functionality of the program is updated, you can create a new executable file with the following steps:
- Delete directories *build* and *dist* from *flask-server* directory.
- Activate a *Poetry* shell with: ```
poetry shell
```
- From *flask-server* directory, run:
```
pyinstaller server.spec
```
- After generating the new executable file, the steps from the [user manual](https://github.com/kodtld/Markov-s-Letters/blob/master/documentation/manual.md) can be followed to run the program.
