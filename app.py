import logging
import datetime
from flask import Flask, request, redirect, make_response, render_template, url_for, jsonify, send_from_directory, Response
import json
import os
from jinja2 import Environment, PackageLoader
import requests
from flask_bootstrap import Bootstrap
from urlparse import urlparse, urlsplit, parse_qs, parse_qsl
import re
import time
env = Environment()

app = Flask(__name__, static_url_path = "/static", static_folder = "static")
Bootstrap(app)

### apidaze Config
base_url = "https://api4.apidaze.io/"

## Demo Variables THIS IS INSECURE, FOR TESTING ONLY!!!
## These are only required if you add in using the REST API
## You can leave as is otherwise
api_key = "<YOUR API KEY>"
api_secret = "<YOUR API SECRET>"
number = "<YOUR APIDAZE NUMBER>"

def timeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

@app.route('/receiveSMS')
def inbound_sms(rec_name):
    url = request.url
    app_url = request.host_url
    this_url = request.base_url
    args = json.loads(request.get_data())
    fromnumber = str(args['caller_id_number'])
    tonumber = str(args['destination_number'])
    text = args['text']
    ts = int(time.time())
    print text
    return "received"

@app.route('/recieveCall')
def inbound_call():
    url = request.url
    app_url = request.host_url
    this_url = request.base_url
    fromnumber = str(request.args.get('caller_id_number'))
    tonumber = request.args.get('destination_number')
    ts = int(time.time())
    example_variable = "stuff"
    template = render_template('call.xml', some_variable=example_variable)
    response = make_response(template)
    response.headers['Content-Type'] = 'text/xml'
    return response

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
