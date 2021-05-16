
from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

import locale
import requests
from bs4 import BeautifulSoup
from datetime import datetime

import pymysql


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Connect to the database
conn = pymysql.connect(host='localhost',
                    user='root',
                    password='hote9142401!',
                    database='ibks',
                    charset='utf8mb4',
                    )

cursor = conn.cursor()

from .common import login_required
from . import member, apply, addon