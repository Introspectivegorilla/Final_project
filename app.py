

import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3



app = Flask(__name__)



db = SQL("sqlite:///flashcards.db")
app.secret_key = 'your secret key'

#session uses file system instead of cookies (?) look this up later 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT , username VARCHAR(30), hash)")
#db.execute("DELETE FROM users")

@app.route ("/")
def home():
    
    return render_template('login.html')

@app.route("/login", methods=["GET","POST"]) #methods get/post allows us to retrieve and send information from forms (user input) 
def login():

    session.clear() #Forgets any user id. For some reason. That I do not know.

    if request.method == "POST":
        if not request.form.get("username"):
            print("well shit")
            return render_template('apology.html',apology_message="Enter an actual username.")
        elif not request.form.get("password"):
            return render_template('apology.html',apology_message="Enter an actual password.")
            print("Hey u cheat")
        
    
    check_table = db.execute("SELECT * FROM users WHERE username=?",request.form.get("username"))
    print(check_table)
    if len(check_table) == 1:
        if check_password_hash(check_table[0]['hash'], request.form.get("password")):
            return render_template('home.html')
        else:
            return render_template('apology.html',apology_message="Incorrect password. Sorry dude.")
    else:
        return render_template('apology.html',apology_message="That username isn't in our database.")
    #print(check_table)
 


@app.route("/register",methods=["GET","POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        check_table = db.execute("SELECT * FROM users WHERE username=?",username)
        print(check_table)
        if len(check_table) != 0:
            return render_template('apology.html',apology_message="Sorry! That username was taken")
        else:
            password = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)",username,password)
            return render_template("login.html")
    else:
        return render_template("login.html")






