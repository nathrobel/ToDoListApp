from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)