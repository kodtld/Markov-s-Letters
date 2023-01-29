"""
Flask application for the backend.
Used to manage routes and to use functions.
"""
from flask import Flask
from services.trie_service import Trie
app = Flask(__name__)

@app.route("/variables")
def variables():
    """
    Placeholder function
    """
    trie = Trie()
    string = str(trie.search("Our"))
    return string

if __name__ == "__main__":
    app.run(debug=True)
