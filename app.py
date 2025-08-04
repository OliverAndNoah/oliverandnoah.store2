from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debug=True watches for file changes and reloads automatically
    app.run(debug=True, port=5000)
