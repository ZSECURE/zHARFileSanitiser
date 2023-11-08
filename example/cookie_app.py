#!/usr/bin/python3

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response("This page sets cookies!")
    resp.set_cookie('cookie1', 'value1')
    resp.set_cookie('cookie2', 'value2')
    resp.set_cookie('cookie3', 'value3')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
