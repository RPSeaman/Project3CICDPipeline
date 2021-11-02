from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") 
def index():
    return ("Welcome to the App in bare-bone state!",render_template("form.html"))


if __name__ == "__main__":
    app.run(debug = True)
 