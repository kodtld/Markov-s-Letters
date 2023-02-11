"""
Flask application for the backend.
Used to manage routes and to use functions.
"""
from flask import Flask, render_template, request
from services.trie_service import Trie
from services.markov_service import MarkovChain

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index(): # word=None, state=1
    """
    Placeholder function
    """
    trie = Trie()
    trie.insert_books()
    markov = MarkovChain(trie)
    sentences = []
    if request.method == "POST":
        pass
    for i in range(10): # pylint: disable=W0612
        string = str(markov.generate_sentence())
        sentences.append({"sentence": string})

    return render_template('index.html', sentences = sentences)

# def one_state(markov, word=None):
#     pass

# def two_state(markov, word=None):
#     pass

# def three_state(markov, word=None):
#     pass


if __name__ == "__main__":
    app.run(debug=True)
