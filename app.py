from flask import Flask,render_template,request,redirect

app = Flask(__name__)
tasks = []
#Read
@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    
    return render_template("index.html",tasks= tasks)

#Create
@app.route("/add", methods = ["POST"])
def add():
    new_task = request.form["task"]
    task_id = len(tasks)+1
    tasks.append({"id": task_id, "task": new_task})
    
    return redirect("/")

#Delete
@app.route("/delete", methods = ["POST"])
def delete():
    task_id = int(request.form["task_id"])
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    
    return redirect("/")

#Update
@app.route("/update", methods = ["POST"])
def update():
    task_id = int(request.form["task_id"])
    updated_text = request.form["updated_task"]
     
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = updated_text
            break
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)