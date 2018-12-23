from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__, template_folder="templates")
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def submit():
    
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 3:
        flash("Name must be 3+ characters", 'name')
    
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    elif len(request.form['comment']) > 120:
        flash("Comment must be less than 120 characters", 'comment')
            
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']

        return redirect("/success")

@app.route('/success')
def success():
    
 
    return render_template("index1.html")

if __name__=="__main__":
    app.run(debug=True)