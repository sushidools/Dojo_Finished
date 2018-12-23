"""
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')  # Notice that we changed where we redirect to
                              # Now we go to the page that displays the name and email!

@app.route('/show')
def show_user():
    if 'name' in session:
        print('name exists!')
    else:
        print("key 'name' does NOT exist")
    return render_template('user.html')

if __name__=="__main__":
    # run our server
    app.run(debug=True, port=3000)
""" 
