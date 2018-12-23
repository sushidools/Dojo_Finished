from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, template_folder="templates")
app.secret_key = 'ThisIsSecret'
import random
import datetime
# our index route will handle rendering our form
@app.route('/')
def index():
    if "myGold" not in session or "activity" not in session:
        session["myGold"] = 0
        session["activity"] = []
    elif "myGold" in session:
        pass
    print(session)
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process_gold', methods=['POST'])
def income():
    date = datetime.datetime.now().strftime("%Y/%m/%d %X %p")
    #print(date)
    temp = session['activity']
    if request.form['building'] == 'farm':
        gold = random.randint(10,21)
        session['myGold'] = int(session['myGold']) + gold
        temp.append("You found " + str(gold) + ". (" + date + ")")
    elif request.form['building'] == 'cave':
        gold = random.randint(5,11)
        session['myGold'] = int(session['myGold']) + gold
        temp.append("You found " + str(gold) + ". (" + date + ")")
    elif request.form['building'] == 'house':
        gold = random.randint(2, 6)
        session['myGold'] = int(session['myGold']) + gold
        temp.append("You found " + str(gold) + ". (" + date + ")")
    elif request.form['building'] == 'casino':
        gold = random.randint(-50, 51)
        session['myGold'] = int(session['myGold']) + gold
        if gold < 0 :
            temp.append("You have lost " + str(gold) + "! (" + date + ")")
        else:
            temp.append("You got lucky and won " + str(gold) + ". (" + date + ")")
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    # run our server
    app.run(debug=True) 
