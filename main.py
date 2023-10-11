from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
from datetime import date
import requests
import test
import json

api_key = 'YOUR_API_KEY'
symbols = ['MSFT', 'GOOGL', 'UBER']
stock_prices = []
for symbol in symbols:
    response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}')
    data = response.json()
    try:
        low_price = data['Global Quote']['04. low']
        high_price = data['Global Quote']['03. high']
        current_price = data['Global Quote']['05. price']
        stock_prices.append([symbol, low_price, high_price, current_price])
    except KeyError:
        print("Key Error")


lst = []
app = Flask(__name__)
app.secret_key = os.urandom(24)

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="login_details")
    cursor = conn.cursor()
    print("Server online")
except:
    print("cannot connect to server")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login3.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def dashboard():
    global stock_prices
    headers = ('Stock Name', 'High', 'Low', 'Current Price')
    if 'user_id' in session:
        return render_template('home.html', headers=headers, data=stock_prices)
    else:
        return redirect('/')


@app.route('/profile')
def profile():
    global lst
    cursor.execute("""SELECT * FROM `user_details` WHERE `U_email` LIKE '{}'""".format(lst[0]))
    users = cursor.fetchall()
    print(users)
    print(lst)
    if users[0][6] == "Yes":
        return render_template('profile2.html', data=users)
    else:
        return render_template("profile.html", data=users)


@app.route('/login_validation', methods=['POST'])
def login_validation():
    global lst
    email = request.form.get('email')
    password = request.form.get('password')
    lst.append(email)
    lst.append(password)
    cursor.execute(
        """SELECT * FROM `user_details` WHERE `U_email` LIKE '{}' AND `U_pass` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    birth = request.form.get('DOB')
    sex = request.form.get('gender')

    cursor.execute("""INSERT INTO `user_details` (`user_ID`,`U_name`,`U_email`,`U_pass`,`U_DOB`,`U_Gender`) 
    VALUES(NULL,'{}','{}','{}','{}','{}')""".format(name, email, password, birth, sex))

    conn.commit()
    cursor.execute("""SELECT * FROM `user_details` WHERE `U_email` LIKE '{}'""".format(email))
    myuser = cursor.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/home')


@app.route('/comment')
def comment():
    return render_template('comment.html')


@app.route('/accept_comment', methods=['POST'])
def acc_comment():
    global lst
    today = date.today()
    comment = request.form.get('comment')
    cursor.execute("""SELECT user_ID FROM `user_details` WHERE `U_email` LIKE '{}'""".format(lst[0]))
    myuser = cursor.fetchone()
    print(myuser[0])
    cursor.execute("""INSERT INTO `comment_details`(`user_ID`, `date`,`comment`) 
    VALUES ({},'{}','{}')""".format(myuser[0], today, comment))
    conn.commit()
    return redirect('/comment')

@app.route('/graph1')
def plot_graph3():
    test.google()
    return render_template("google.html")


@app.route('/graph2')
def plot_graph2():
    test.uber()
    return render_template("uber.html")

@app.route('/graph3')
def plot_graph1():
    test.msft()
    return render_template('msft.html')


@app.route('/predict')
def predict():

    return render_template("predict.html")

@app.route('/logout')
def logout():
    global lst
    lst.clear()
    session.pop('user_id')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
