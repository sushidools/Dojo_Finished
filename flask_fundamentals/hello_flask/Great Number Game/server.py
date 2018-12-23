from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__, template_folder="templates")
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    rannum = random.randint(0, 100)
    guess = session[request.form['text']]
    print(guess)
    if
        
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)