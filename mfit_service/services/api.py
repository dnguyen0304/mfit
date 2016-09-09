# -*- coding: utf-8 -*-

import flask
import flask_restful

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

