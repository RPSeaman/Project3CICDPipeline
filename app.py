from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route("/") 
def index():
    return render_template("form.html" ,tasks = tasks)

@app.route("/add",methods=["POST"])
def add():
    now  = datetime.now()
    
    task = request.form.get("task")
    tasks.append(task)
    print(tasks[-1])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
 