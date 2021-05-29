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

        if param:
            return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        else :
            return datetime.today().strftime('%Y-%d-%m')

    if request.method == 'GET':
        return '''<h1>Marvik</h1>
        <p>Using the latest technology, processes and tools, we create custom solutions to find invisible insights and trends within your organization’s data. Differentiate from yourselves from the competition by scaling your business while reducing costs.</p>'''


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



if __name__ == "__main__":
    app.run()
