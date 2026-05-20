from flask import Flask,render_template,request,redirect

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    
    return render_template("index.html",tasks= tasks)

@app.route("/add", methods = ["POST"])
def add():
    new_task = request.form["task"]
    task_id = len(tasks)+1
    tasks.append({"id": task_id, "task": new_task})
    
    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete():
    task_id = int(request.form["task_id"])
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)