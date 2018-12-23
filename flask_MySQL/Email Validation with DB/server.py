from flask import Flask, flash, redirect, render_template, request, url_for, session
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__, template_folder="templates")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'randomstring'
mysql = connectToMySQL('emailvalidationdb')

@app.route('/', methods=['GET'])
def index():
    mysql = connectToMySQL("emailvalidationdb")
    all_emails = mysql.query_db("SELECT * FROM emails")

    return render_template("index.html", emails = all_emails)

@app.route('/email', methods=['POST'])
def create():
    email = request.form['email']
    mysql = connectToMySQL("emailvalidationdb")
    query = "SELECT * FROM emails WHERE email = some_email"
    data = {
        'some_email': request.form['email']
    }
    email = request.form['email']
    if len(email) < 1:
        flash("Email cannot be blank!", 'error')
        return redirect('/')
    if mysql.query_db(query, data):
        mysql = connectToMySQL("emailvalidationdb")
        flash("Email already in use!", 'error')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'error')
        return redirect('/')
    else:
        mysql = connectToMySQL("emailvalidationdb")
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW())"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
    flash('The email address ' + email + ' is a VALID email adress! Thank you!', "success")
    return redirect('/success')

@app.route('/success') 
def show():
    mysql = connectToMySQL("emailvalidationdb")
    query = "SELECT * FROM emails"
    all_email = mysql.query_db(query)
    return render_template('success.html', emails = all_email)

@app.route('/delete_email', methods=["GET","POST"])
def delete_email():
    mysql = connectToMySQL("emailvalidationdb")
    delete_ids = request.form.getlist('do_delete')
    query = 'DELETE FROM emails WHERE id IN (' + ','.join(map(str, delete_ids)) + ')'
    delete_them = mysql.query_db(query)
    return redirect('/')

if __name__ == "__main__":
   app.run(debug = True, port=5055)