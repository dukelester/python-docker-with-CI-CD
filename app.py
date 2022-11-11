""" A simple application with Flask"""

import json

import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """ A simple hello world route"""
    return 'Hello duke lester welcome to Docker and Flask application'

@app.route("/welcome")
def welcome_to_flask():
    """ A simple endpoint for welcomming users to Flask"""
    return "<h3>Welcome to flask developemnt </h3>"

@app.route("/products")
def all_products():
    "A simple endpoint for a list of products in the store"
    return [
        {"name": "Sample product", "description": "A simple product for users",
        "price": 4000, "shop owner": "duke lester", "location": "Juja"},
        {"name": "Sample product 2", "description": "A simple product for users",
        "price": 79000, "shop owner": "duke lester", "location": "Juja"},
        {"name": "Sample product 3", "description": "A simple product for users",
        "price": 7809, "shop owner": "duke lester", "location": "Juja"},
        {"name": "Sample product 4", "description": "A simple product for users",
        "price": 7800, "shop owner": "duke lester", "location": "Juja"},
        {"name": "Sample product 5", "description": "A simple product for users",
        "price": 500, "shop owner": "duke lester", "location": "Juja"},
        ]
@app.route("/widgets")
def get_widgets():
    """ Connect to the database and Get the widgets from the database"""
    mydb = mysql.connector.connect(
        host="mysqldb", user="root",port=32000,
        password="duke2030", database="inventory",
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM widgets")
    row_headers = [x[0] for x in cursor.description] # Get the headers
    results = cursor.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in results]
    print(json_data, "The data")
    cursor.close()
    return json.dumps(json_data)

@app.route("/initdb")
def init_db():
    """ Initialize the database """
    mydb = mysql.connector.connect(
        host="mysqldb", user="root",port=32000,
        password="duke2030", database="inventory",
        )
    cursor = mydb.cursor()
    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("CREATE DATABASE widgets (name  VARCHAR(255), description  VARCHAR(255))")
    cursor.close()
    return 'initialize the database'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
