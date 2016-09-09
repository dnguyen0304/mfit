# -*- coding: utf-8 -*-

import flask_restful

import mfit_service
from mfit_service import services


# TODO (duyn): What constitutes a transaction?
class Base(flask_restful.Resource):

    def __init__(self):
        super().__init__()

        self._db_context_factory = services.DBContextFactory(
            connection_string=mfit_service.configuration['repositories']['PostgreSQL']['connection_string'])
        self._db_context = self._db_context_factory.create()

