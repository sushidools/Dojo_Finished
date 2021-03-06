from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__, template_folder="templates")
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/process", methods=['POST'])
def submit():
    # adding validation rules
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
    elif len(request.form['comment']) > 100:
        flash("Comment must be less than 100 characters", 'comment')
            
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect("/success")
if __name__=="__main__":
    app.run(debug=True)