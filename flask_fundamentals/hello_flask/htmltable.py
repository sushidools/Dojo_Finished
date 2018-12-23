"""
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def table():
    users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
);
    return render_template("index2.html", users = users )

if __name__=='__main__':
    app.run(debug=True)
"""
#Only problem with all of this commenting out is that if I were to want to run them again then I would need to uncomment what I want and recomment out what has the same adress
#or i could start changing the localhost location
#like instead of 5000 i could use 3000 or any other 4 numbers
