from flask import Flask

app = Flask(__name__)

@app.route("/variables")
def variables():
    return {"variables": ["Var1", "Var2", "Var3"]}

if __name__ == "__main__":
    app.run(debug=True)