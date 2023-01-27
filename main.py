from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello_world():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/homerun', methods = ["POST"])
def homerun():
    this_message = request.form.get("text1")
    print(this_message)
    return render_template('homerun.html', message = this_message)
    
