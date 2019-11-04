from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key="qwertyuiop"

@app.route('/')
def hello_world():
    session={}
    gold ="gold"
    # if request.method =="GET":
    if "gold" not in session:
        session["gold"]= 0
    if "counter" not in session:
        session["counter"]=0
    if "activities" not in session:
        session["activities"]=[]
        # gold == session
    return render_template("index.html")

@app.route("/process", methods=["POST"])

def processgold():
    date_time = datetime.now()
    print(request.form)
    if request.form["building"] == "farm":
            place = "farm"
            gold = random.randint(10,20)
            session["gold"]+= gold
            session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            session['activities'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "cave":
            place =  "cave"
            gold = random.randint(5,10)
            session['gold']+= gold
            session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            session['activities'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "house":
            place = "house"
            gold =random.randint(2,5)
            session['gold']+= gold
            session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            session['activities'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "casino":
            place = "casino"
            gold = random.randint(0,100) -50
            session['gold']+= gold
            session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            session['activities'].insert(0,message)
            return redirect('/')
        return redirect('/')


if __name__=="__main__":
    app.run(debug=True)