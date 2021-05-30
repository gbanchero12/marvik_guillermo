# -*- coding: utf-8 -*-
import flask
from flask import request, json
from datetime import datetime
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        param = request.json['booleanParam']
        return datetime.today().strftime('%Y-%m-%d %H:%M:%S') if param else datetime.today().strftime('%Y-%d-%m')        

    if request.method == 'GET':
        return '''<h1>Working ok ...</h1>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run()
