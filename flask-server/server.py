"""
Flask application for the backend.
Used to manage routes and to use functions.
"""
from flask import Flask, render_template, request
from services.trie_service import Trie
from services.markov_service import MarkovChain

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index(prompt=None, state=1):
    """
    Placeholder function
    """
    trie = Trie()
    trie.insert_books()
    markov = MarkovChain(trie)
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
        prompt = request.form['prompt']
        if state == 1:
            sentences = one_state(markov,prompt)
            return render_template('index.html', sentences = sentences)

        if state == 2:
            sentences = two_state(markov,prompt)
            return render_template('index.html', sentences = sentences)

        # if state == 3:
        #     pass

    return render_template('index.html', sentences = sentences)

def one_state(markov, prompt=None):
    """
    Generates and returns dictionary of one-state Markov sentences
    """
    sentences = []
    for i in range(6): # pylint: disable=W0612
        if prompt == "":
            string = str(markov.generate_sentence())
        else:
            string = str(markov.generate_sentence(prompt))
        sentences.append({"sentence": string})
    return sentences

def two_state(markov, prompt=None):
    """
    Generates and returns dictionary of two-state Markov sentences
    """
    sentences = []
    for i in range(6): # pylint: disable=W0612
        if prompt == "" or len(prompt.split()) != 2:
            string = str(markov.generate_two_sentence())
        else:
            print("ala")
            string = str(markov.generate_two_sentence(prompt))
        sentences.append({"sentence": string})
    return sentences

# def three_state(markov, prompt=None):
#     pass


if __name__ == "__main__":
    app.run(debug=True)
