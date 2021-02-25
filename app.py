from flask import Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World from Niloy"


if __name__ == "__main__":
    app.run(debug=True)
