from flask import render_template, request
from app import app
from schedule_api import *
import string

'''
TERMS
'''
@app.route('/')
def index():
    Variables = {}

    return render_template('index.html', **Variables)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404