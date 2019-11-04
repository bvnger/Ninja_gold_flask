from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key="qwertyuiop"

@app.route('/')
def hello_world():
    session={}
    gold ="gold"
    if gold not in session:
        session["gold"]= 0
        gold == session
    return render_template("index.html")

@app.route("/process", methods=["POST"])

def processgold():
    date_time = datetime.now()
    if request.method == "POST":
        if request.POST["building"] == "farm":
            


    pass




if __name__=="__main__":
    app.run(debug=True)