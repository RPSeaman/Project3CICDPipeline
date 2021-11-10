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
    newTask = task.Task(title,[])
    tasks.append(newTask)
    #print(tasks[-1].getTitle()," ",tasks[-1].getDate())

    return redirect(url_for("index"))


@app.route("/remove/<string:name>")
def remove(name):
    print(name)
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            tasks.remove(tasks[i])
            break
    return redirect(url_for("index"))
    
@app.route("/updatePriority/<string:name>", methods=["POST"])
def updatePriority(name):
    print(name)
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            print(i)
            break
    tasks[i].changePriority(request.form.get(tasks[i].getTitle()))
    return redirect(url_for("index"))

@app.route("/updateStatus/<string:name>", methods=["POST"])
def updateStatus(name):
    print(name)
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            print(i)
            break
    tasks[i].changeStatus(request.form.get(tasks[i].getTitle()))
    return redirect(url_for("index"))



@app.route("/addTag/<string:name>", methods=["POST"])
def addTag(name):
    print(name)
    for i in range(len(tasks)):
        if tasks[i].getTitle()==name:
            print(i)
            break
    print(tasks[i].getTags())
    tasks[i].getTags().append(request.form.get(tasks[i].getTitle()))
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug = True)
 