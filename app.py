from flask import Flask, render_template, request, redirect,url_for
import task

app = Flask(__name__)

tasks =[]

@app.route("/") 
def index():
    return render_template("form.html",tasks = tasks)

@app.route("/add", methods=["POST"])
def add():

    
    title = request.form.get("task")
    print(title)
    newTask = task.Task(title)
    tasks.append(title)
    #print(tasks[-1].getTitle()," ",tasks[-1].getDate())

    return redirect(url_for("index"))


@app.route("/remove/<string:name>")
def remove(name):
    tasks.remove(name)
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug = True)
 