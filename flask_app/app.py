from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    quote = requests.get("http://fastapi_service:8000/quote").json()
    return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
