from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__, template_folder="templates")
app.secret_key = "ThisIsSecret!"

mysql = connectToMySQL('usersdb')
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    debugHelp("INDEX METHOD")
    if 'logged_in' in session.keys():
        return redirect('/success')
    else:
        return render_template("index.html")
   
@app.route("/register", methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    session['email'] = request.form['email']
    # Let's add validtion rules
    mysql = connectToMySQL('usersdb')
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {
        "email" : request.form['email']
    }
    result = mysql.query_db(query, data)
    print(result)
    if result:
        flash("Email address already exists!", "email")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')

    if len(request.form['first_name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['first_name']) <= 3:
        flash("Name must be 3+ characters", 'first_name')

    if len(request.form['last_name']) < 1:
        flash("Name cannot be blank!", 'last_name')
    elif len(request.form['last_name']) <= 3:
        flash("Name must be 3+ characters", 'last_name')
    
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters", "password")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Passwords must match", "password_match")
            
    debugHelp('RESERVE METHOD')
    # return "reserve"
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)

        mysql = connectToMySQL("usersdb")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, NOW(), NOW());"
        data = { 
            "first_name"    : request.form['first_name'],
            "last_name"     : request.form['last_name'],
            "email"         : request.form['email'],
            "password_hash" : pw_hash
        }

        mysql.query_db(query, data)
        return redirect("/success")

@app.route('/login', methods=["POST"])
def login():
    mysql = connectToMySQL("usersdb")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form["login"] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['log_pass']):
            session['userid'] = result[0]['id']
            session['first_name'] = result[0]['first_name']
            session['logged_in'] = '1'
            # never render on a post, always redirect!
            return redirect('/success')
    # if unable to login flash and redirect
    flash("You could not be logged in", "login")
    return redirect("/")
  
@app.route("/success", methods=['GET', 'POST'])
def success():
    flash("Success you have been registered.")
    return render_template("profile.html")
  
def debugHelp(message = ""):
    print("\n\n-----------------------", message, "--------------------")
    #print('REQUEST.FORM:', request.form) this shouldn't show because it prints the form password
    print('SESSION:', session)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)