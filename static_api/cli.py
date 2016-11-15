# -*- coding: utf-8 -*-

import click
import json

from flask import Flask, jsonify
from flask_cors import cross_origin


api = Flask(__name__)
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
@cross_origin
def get_dir(path):
    path = path.rstrip('/')
    r = open_data_file(FILE_PATH + '/' + path + '.json')
    return jsonify(r)


@click.command()
@click.argument('static_path')
def main(static_path):
    """Console script for static_api"""
    click.echo(static_path)
    global FILE_PATH
    FILE_PATH = static_path
    api.run()


if __name__ == "__main__":
    main()
