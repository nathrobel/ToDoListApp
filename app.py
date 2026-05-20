from flask import Flask,render_template,request,redirect

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    
    return render_template("index.html",tasks= tasks)

@app.route("/add", methods = ["POST"])
def add():
    #“Go into the templates folder, find index.html, and send it to the browser.
     # get data from form
    task = request.form["task"]
    tasks.append(task)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)