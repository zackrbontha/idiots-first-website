from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)