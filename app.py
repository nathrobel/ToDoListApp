from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    tasks = ["Buy milk", "Study Flask"]
    return render_template("index.html",tasks= tasks)

if __name__ == "__main__":
    app.run(debug=True)