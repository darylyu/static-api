# -*- coding: utf-8 -*-
from flask import Flask
api = Flask(__name__)

@api.route('/', defaults={'url': ''})
@app.route('/<url:url>')
def get_dir(url):
    return url
