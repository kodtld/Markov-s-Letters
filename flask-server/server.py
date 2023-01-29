from flask import Flask
from services.trie_service import Trie
app = Flask(__name__)

@app.route("/variables")
def variables():
    t = Trie()
    k = str(t.startsWith("Our"))
    return k

if __name__ == "__main__":
    app.run(debug=True)