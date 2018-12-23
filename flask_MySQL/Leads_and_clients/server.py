from flask import Flask, render_template, request, redirect
app = Flask(__name__, template_folder="templates")
# our index route will handle rendering our form
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('clientsleadsdb')
# now, we may invoke the query_db method
print("all the customers and leads", mysql.query_db("SELECT * FROM customers;"))
@app.route('/')
def index():
    mysql = connectToMySQL("clientsleadsdb")
    all_customers = mysql.query_db("SELECT * FROM customers")
    print("Fetched all customers", all_customers)
    return render_template('index.html', customers = all_customers)

@app.route('/create_lead', methods=['POST'])
def create():
    mysql = connectToMySQL("clientsleadsdb")
    query = "INSERT INTO customers (full_name, leads, created_at, updated_at) VALUES (%(full_name)s, %(leads)s, NOW(), NOW());"
    data = {
             'full_name': request.form['full_name'],
             'leads':  request.form['leads']
           }
    new_customer_id = mysql.query_db(query, data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True, port=4040)