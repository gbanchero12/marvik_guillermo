# -*- coding: utf-8 -*-
import flask
from flask import request, json
from datetime import datetime
from werkzeug.exceptions import HTTPException

# Flask initialization:
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Handling requests:
@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
            # Reading the request body by the param 'booleanParam'
            param = request.json['booleanParam']             
            # Returning the formatted date depending by the param received
            return datetime.today().strftime('%Y-%m-%d %H:%M:%S') if param else datetime.today().strftime('%Y-%d-%m')        
        
        if request.method == 'GET':
            return '''<h1>Working ok ...</h1>'''

# Handling errors:

# 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Mapping JSON instead of HTML for HTTP errors:
@app.errorhandler(HTTPException)
def handle_exception(e):    
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run()
