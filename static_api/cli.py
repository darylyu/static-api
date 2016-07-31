# -*- coding: utf-8 -*-

import click
import json

from flask import Flask, jsonify


api = Flask(__name__)
FILE_PATH = '.'


def open_data_file(file_path):
    with open(file_path) as fp:
        r = json.load(fp)
        return r


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
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
