# -*- coding: utf-8 -*-

import flask_restful

import mfit
from mfit import app


class BaseCollection(flask_restful.Resource):

    def __init__(self):
        super().__init__()

        self._db_context_factory = app.DBContextFactory(
            connection_string=mfit.configuration['repositories']
                                                ['PostgreSQL']
                                                ['connection_string'])
        self._db_context = self._db_context_factory.create()

