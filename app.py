

import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3



app = Flask(__name__)


db = SQL("sqlite:///flashcards.db")
app.secret_key = 'your secret key'

# session uses file system instead of cookies (?) look this up later
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
#db.execute("DROP TABLE flashcards")
#db.execute("DROP TABLE cardsets")

db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT , username VARCHAR(30), hash)")


sets = db.execute("CREATE TABLE IF NOT EXISTS cardsets (set_name VARCHAR(25), set_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id))")

cards = db.execute("CREATE TABLE IF NOT EXISTS flashcards (prompt TEXT NOT NULL, response TEXT NOT NULL, card_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT,set_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id),FOREIGN KEY (set_id) REFERENCES cardsets(set_id))")




@app.route("/")
def home():

    return render_template('login.html')


# methods get/post allows us to retrieve and send information from forms (user input)
@app.route("/login", methods=["GET", "POST"])
def login():

    # Forgets any user id. For some reason. That I do not know.
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            print("well shit")
            return render_template('apology.html', apology_message="Enter an actual username.")
        elif not request.form.get("password"):
            return render_template('apology.html', apology_message="Enter an actual password.")
            print("Hey u cheat")

    check_table = db.execute(
        "SELECT * FROM users WHERE username=?", request.form.get("username"))
    print(check_table)
    if len(check_table) == 1:
        if check_password_hash(check_table[0]['hash'], request.form.get("password")):
            session['user_id'] = check_table[0]['user_id']

            return render_template('home.html')
        else:
            return render_template('apology.html', apology_message="Incorrect password. Sorry dude.")
    else:
        return render_template('apology.html', apology_message="That username isn't in our database.")
    # print(check_table)


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        check_table = db.execute(
            "SELECT * FROM users WHERE username=?", username)
        print(check_table)
        if len(check_table) != 0:
            return render_template('apology.html', apology_message="Sorry! That username was taken")
        else:
            password = generate_password_hash(password)
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?,?)", username, password)
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/new',methods=["GET", "POST"])
def new():

    if request.method == "POST":
        prompts = request.form.getlist('prompt')
        responses = request.form.getlist('response')
        title = request.form.get('title')

        study_dict = {key: value for key, value in zip(prompts, responses)}
        #print(study_dict)

        set_id = db.execute("INSERT INTO cardsets (user_id, set_name) VALUES (?, ?)", session['user_id'], title)
        #print(set_id)
        for key, value in study_dict.items():
            test=db.execute("INSERT INTO flashcards (prompt, response, user_id, set_id) VALUES (?,?,?,?)",key,value,session['user_id'],set_id)

        #all_cards = db.execute("SELECT * FROM flashcards")
        #set_front = db.execute("SELECT * FROM cardsets")
        #print(set_front)

        #print(all_cards)
        return render_template('home.html')
    else:
        return render_template('new.html')

@app.route('/library')
def library():

    all_cards = db.execute("SELECT * FROM flashcards")
    set_front = db.execute("SELECT * FROM cardsets")

    return render_template('library.html',all_cards=all_cards,set_front=set_front)

@app.route('/play<int:set_id>')
def play(set_id):

    load_set = db.execute("SELECT * FROM cardsets WHERE set_id =?",set_id)
    load_cards = db.execute("SELECT * FROM flashcards WHERE set_id=?",set_id)


    return render_template('play.html',load_set=load_set,load_cards=load_cards)