from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def hello_world():
    if request.method == "GET":
        return render_template('index.html')
    else:
        message = request.form.get("text1")
        return render_template('homerun.html')

@app.route('/homerun', methods = ["GET"])
def homerun():
    return render_template("homerun.html")
