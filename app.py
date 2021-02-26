from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def get_result(query):

    url = 'https://google.com/search?q=filetype:pdf+' + query.replace(" ", "+")

    content = requests.get(url)
    soup = BeautifulSoup(content.text, "lxml")
    url_list = []
    name_list = []

    for item in soup.select("a"):
        f_url = item.get("href")
        myurl = f_url.replace(f_url[:7], "")
        myurl = myurl.split("&")
        myurl = myurl[0]
        if (".pdf" in myurl):
            url_list.append(str(myurl))

    headline_texts = soup.find_all("h3")
    for headline_text in headline_texts:
        name_list.append(
            str(headline_text.getText().replace("[PDF]", "").strip()))

    url_list.reverse()
    name_list.reverse()

    l = []
    for i in range(len(url_list)):
        d = {}
        d["title"] = name_list[i]
        d["url"] = url_list[i]
        l.append(d)
    l.reverse()
    return l


@app.route("/api/<string:query>", methods=["GET"])
def initial_api(query: str):
    if request.method == "GET":
        if " " in query:
            query = query.replace(" ", "+")
        else:
            pass

        return jsonify(get_result(query=query))


if __name__ == "__main__":
    app.run()
