
from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder="templates")  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    blackberry = request.form['blackberry']
    strawberry = request.form['strawberry']
    x = int(apple) + int(raspberry) + int(blackberry) + int(strawberry)
    print(request.form)
    return render_template("checkout.html", x=x)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   
