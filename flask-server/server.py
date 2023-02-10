"""
Flask application for the backend.
Used to manage routes and to use functions.
"""
from flask import Flask
from services.trie_service import Trie
from services.markov_service import MarkovChain

app = Flask(__name__)

@app.route("/")
def index(word=None):
    """
    Placeholder function
    """
    trie = Trie()
    trie.insert_books()
    markov = MarkovChain(trie)
    words = []
    for i in range(10): # pylint: disable=W0612
        string = str(markov.generate_two_sentence(starting_word=word))
        words.append({"sentence": string})
    return words

if __name__ == "__main__":
    app.run(debug=True)
