from flask import Flask,render_template,request,redirect
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(
    dbname="todoapp",
    user="nathanrobel",
    host="localhost",
    password=""
)

conn.autocommit = True
cur = conn.cursor()

#Read
@app.route("/")
def home():
    #“Go into the templates folder, find index.html, and send it to the browser.
    cur.execute("SELECT id, task FROM tasks ORDER BY id")
    rows = cur.fetchall()

    tasks = [
        {"id": r[0], "task": r[1]} for r in rows
    ]

    
    
    return render_template("index.html",tasks= tasks)

#Create
@app.route("/add", methods = ["POST"])
def add():
    task = request.form["task"]

    cur.execute(
        "INSERT INTO tasks (task) VALUES (%s)",
        (task,)
    )

    
    
    return redirect("/")

#Delete
@app.route("/delete", methods = ["POST"])
def delete():
    task_id = int(request.form["task_id"])
    cur.execute("DELETE FROM tasks where id =%s",(task_id,))
    
    return redirect("/")

#Update
@app.route("/update", methods = ["POST"])
def update():
    task_id = int(request.form["task_id"])
    updated_text = request.form["updated_task"]
     
    cur.execute(
        "UPDATE tasks SET task = %s WHERE id = %s",
        (updated_text, task_id)
    )
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)