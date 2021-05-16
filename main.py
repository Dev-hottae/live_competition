# /app.py
from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

import locale
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from app import app




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