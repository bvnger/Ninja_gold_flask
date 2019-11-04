from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
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
            place = random.randint(10,20)
            request.session['gold']+= gold
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            request.session['activites'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "cave":
            place = random.randint(5,10)
            request.session['gold']+= gold
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            request.session['activites'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "house":
            place = random.randint(2,5)
            request.session['gold']+= gold
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            request.session['activites'].insert(0,message)
            return redirect('/')
    if request.method == "POST":
        if request.POST["building"] == "casino":
            place = random.randint(0,100) -50
            request.session['gold']+= gold
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"  
            request.session['activites'].insert(0,message)
            return redirect('/')
        return redirect('/')



    pass




if __name__=="__main__":
    app.run(debug=True)