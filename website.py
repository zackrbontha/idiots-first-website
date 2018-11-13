from flask import Flask, request, render_template
from testo import spam
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/omega")
def test():
	return spam()
	

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)