#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import jsonify


app = Flask(__name__)
DATABASE = 'linggle.db'


def connect_to_database():
    return sqlite3.connect(DATABASE)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/search", methods=['GET'])
def get_query_string():
    import query
    q = request.args.get('query', 0, type=str)
    qq = query.deal_query(q)
    cur = get_db().cursor()
    r = query.query_result3(cur, qq)
    print 'result :{}'.format(r)
    return jsonify(result=r)


@app.route("/")
def root():
    return render_template('index.html', head_name='hello')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
