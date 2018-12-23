"""
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/play')
def play():
    return render_template("index.html", number=3)

@app.route('/play/<number>/<color>')
def box_color(number, color = "blue"):
    return render_template("index.html", number=int(number), box_color=color)

if __name__=='__main__':
    app.run(debug=True)
"""