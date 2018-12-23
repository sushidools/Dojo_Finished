"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def alpha():
    return "Hello World!"

@app.route('/dojo')
def beta():
    return "Dojo!"

@app.route('/say/<name>') #for this it will take any of the input and capitalize it
def say(name):
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<number>/<word>')
def repeat(number, word): 
    return (word + " ") * int(number) #included the space to see the separation between words returned to the page

if __name__=='__main__':
    app.run(debug=True)
"""