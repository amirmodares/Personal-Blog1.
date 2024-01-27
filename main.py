from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    date = datetime.datetime.now()
    year_site = date.strftime("%Y")
    return render_template("index.html", year=year_site)


@app.route('/guess/<name>')
def guess_page(name):
    url = "https://api.agify.io"
    dic = {
        "name": f"{name}"
    }
    data = requests.get(url=url, params=dic)
    age = data.json()
    return render_template("index.html", age_variable=age["age"])


if __name__ == "__main__":
    app.run(debug=True)