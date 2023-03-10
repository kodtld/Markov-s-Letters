"""
Flask application for the backend.
Used to manage routes and to use functions.
"""

from flask import Flask, render_template, request
from services.trie_service import Trie
from services.markov_service import MarkovChain

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index(starting_prompt=None, state=1):
    """
    Render the index.html template with a list of generated sentences.

    Args:
        prompt (str, optional): A prompt for the Markov chain to generate sentences from.
            Defaults to None.
        state (int, optional): The state (i.e. the order of the Markov chain) to use for
            sentence generation. Defaults to 1.

    Returns:
        str: The rendered HTML template.

    """
    sentences = [
        {'sentence': 'Your'},
        {'sentence': 'Generated'},
        {'sentence': 'Sentences'},
        {'sentence': 'Will'},
        {'sentence': 'Appear'},
        {'sentence': 'Here!'}
        ]

    if request.method == "POST":
        state = int(request.form['slider'])
        starting_prompt = request.form['prompt']
        trie = Trie()
        trie.insert_books()
        markov_chain = MarkovChain(trie, state)
        sentences = call_generate_sentences(markov_chain, starting_prompt)
        return render_template('index.html', sentences = sentences)

    return render_template('index.html', sentences = sentences)

def call_generate_sentences(markov_chain, starting_prompt=None):
    """
    Calls the markov_service and returns dictionary of state Markov sentences

    Parameters:
    markov (MarkovChain): An instance of MarkovChain class
    prompt (str, optional): A string prompt to generate sentences from. Defaults to None.

    Returns:
    list: A list of dictionaries containing generated sentences
    """
    sentences = []
    for i in range(6): # pylint: disable=W0612
        if starting_prompt == "":
            string = str(markov_chain.generate_sentence())
        else:
            string = str(markov_chain.generate_sentence(starting_prompt))
        sentences.append({"sentence": string})
    return sentences

if __name__ == "__main__":
    app.run(debug=True)
