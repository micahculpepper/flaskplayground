#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Main module of flaskplayground. Provides command-line entry point and main logic.
"""

from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/report/')
def report():
    with open('data/data.csv') as f:
        rows = f.readlines()
    html_table_rows = []
    for row in rows:
        html_table_rows.append(
            "<tr><td>" + "</td><td>".join([cell for cell in row.split(",")]) + "</td></tr>"
            )
    return "\n".join(html_table_rows)


# def main(args=None):
#     """CLI entry point"""
#     if not args:
#         import parsers
#         parser = parsers.main()
#         args = parser.parse_args()


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)  # ssl_context='adhoc'
