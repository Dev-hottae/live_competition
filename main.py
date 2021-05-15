# /app.py
from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

import locale
import requests
from bs4 import BeautifulSoup
from datetime import datetime


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('register.html')

@app.route('/signup_pro', methods=['GET', 'POST'])
def signup_pro():

    if request.method == 'POST':

        #### save register to db ####

        ####################

        #### create session#####
        session['user'] = request.form
        #####################

        data = {
            "msg" : "sign up complete!"
        }

        return render_template('alert.html', data=data)

    else:
        return render_template('register.html') 

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_pro', methods=['GET', 'POST'])
def login_pro():

    if request.method == 'POST':
        #### create session#####
        session['user'] = request.form
        #####################
        return redirect(url_for('index'))
    
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():

    # remove the user_id from the session if it's there
    session.clear()

    return redirect(url_for('index'))

@app.route('/joinCompete')
def joinCompete():
    return render_template('application.html')

@app.route('/joinCompete_pro', methods=['GET', 'POST'])
def joinCompete_pro():
    if request.method == 'POST':

        #### save register to db ####

        ####################

        data = {
            "msg" : "apply complete!"
        }

        return render_template('alert.html', data=data)

    else:
        return render_template('application.html') 

@app.route('/graph')
def graph():
    return render_template('graph.html')
    
@app.route('/charts')
def charts():
    return render_template('charts.html')
    
@app.route('/positions')
def positions():
    
    return render_template('positions.html')

@app.route('/backTest')
def backtest():
    return render_template('backTest.html')
    
@app.route('/utilities-animation.html')
def animation():
    return render_template('utilities-animation.html')
    
@app.route('/utilities-border.html')
def border():
    return render_template('utilities-border.html')
    
@app.route('/utilities-other.html')
def other():
    return render_template('utilities-other.html')

    


if __name__=="__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port="5000", debug=True)