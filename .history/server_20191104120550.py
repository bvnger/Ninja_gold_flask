from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key=qwertyuiop

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
    def process():





if __name__=="__main__":
    app.run(debug=True)