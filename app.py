from flask import Flask, render_template, request, redirect,url_for
import task

app = Flask(__name__)

tasks =[]

@app.route("/") 
def index():
    user = {'username':'test'}
    return render_template("form.html",tasks = tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("task")
    newTask = task.Task(title,[])
    tasks.append(newTask)
    #print(tasks[-1].getTitle()," ",tasks[-1].getDate())

    return redirect(url_for("index"))


@app.route("/remove/<string:name>")
def remove(name):
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            tasks.remove(tasks[i])
            break
    return redirect(url_for("index"))
    
@app.route("/addTag/<string:name>", methods=["POST"])
def addTag(name):
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            break
    tasks[i].addTag(request.form.get(tasks[i].getTitle()))
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug = True)
 