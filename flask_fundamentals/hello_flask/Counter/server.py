"""
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, template_folder="templates")
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/increment')
def increment():
    if 'count' in session:
        session['count'] += 2
    else:
        session['count'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
"""