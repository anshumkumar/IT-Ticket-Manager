from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'LoginData.db')

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route('/login_validate', methods=['POST'])
def login_validate():
    email = request.form.get('email')
    password = request.form.get('password')

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    user = cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).fetchall()
    if len(user) > 0:
        return redirect(f'/home?fname={user[0][0]}&lname={user[0][1]}&email={user[0][2]}')
    else:
        return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email') 

    return render_template('home.html', fname=fname, lname=lname, email=email)  


@app.route('/register_user', methods=['POST'])
def register_user():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    ans = cursor.execute("select * from users where email = ? AND password = ?",  (email, password)).fetchall()

    if len(ans) > 0:
        connection.close()
        return render_template('login.html')
    else:
        cursor.execute("INSERT INTO USERS(first_name, last_name, email, password) VALUES (?, ?, ?, ?)", (fname, lname, email, password))
        connection.commit()
        connection.close()
        return render_template('login.html')
   



if __name__ == "__main__":
    app.run(debug=True)


