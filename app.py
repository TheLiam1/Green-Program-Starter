from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/moin")
def moin():
    return "Moin!"


if __name__ == "__main__":
    app.run(port=1337, debug=True)
