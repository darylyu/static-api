# -*- coding: utf-8 -*-

import click
import json

from flask import Flask, jsonify
from flask_cors import CORS


api = Flask(__name__)
cors = CORS(api, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

FILE_PATH = '.'


def open_data_file(file_path):
    with open(file_path) as fp:
        r = json.load(fp)
        return r


@api.route('/favicon.ico')
def get_favicon():
    # This is a work-around. This function makes the error
    # quietly go away.
    #
    # The error was a 500 error because the could
    # would try to look for a file named favicon.ico.json
    return jsonify(None)


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def get_dir(path):
    path = path.rstrip('/')
    r = open_data_file(FILE_PATH + '/' + path + '.json')
    return jsonify(r)


@click.command()
@click.argument('static_path')
@click.option('--port', '-p')
def main(static_path, port):
    """Console script for static_api"""
    click.echo("serving static api in this directory: %s" % static_path)

    if port:
        api_port = int(port)
    else:
        api_port = 5000
    click.echo("port == %s" % api_port)

    global FILE_PATH
    FILE_PATH = static_path
    api.run(debug=True, port=api_port)


if __name__ == "__main__":
    main()
