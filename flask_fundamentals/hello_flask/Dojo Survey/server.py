"""
from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder="templates")
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def result():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # redirects back to the '/' route
    return render_template("index1.html")

@app.route('/danger')
def danger():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True, port=3000) 

"""