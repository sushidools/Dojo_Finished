"""
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def check():
    return render_template("index1.html", x = 8, y = 8)

@app.route('/<x>/<y>')
def checker(x,y):
    return render_template("index1.html", x = int(x), y = int(y))

if __name__=='__main__':
    app.run(debug=True)

"""