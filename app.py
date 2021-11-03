from flask import Flask, render_template, request, redirect,url_for
import task

app = Flask(__name__)

tasks =[]

@app.route("/") 
def index():
    return render_template("form.html")

@app.route("/add")
def add():
    title = request.form.get("visitor")
    print(title)
    newTask = task.Task(title)
    tasks.append(newTask)
    print(tasks[-1].getTitle()," ",tasks[-1].getDate())

    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(debug = True)
 