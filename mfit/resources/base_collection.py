# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful

import mfit
from mfit import app


class BaseCollection(flask_restful.Resource):

    _model = None
    _resource = None
    _resource_collection = None

    def __init__(self):
        super().__init__()

        self._db_context_factory = app.DBContextFactory(
            connection_string=mfit.configuration['repositories']
                                                ['PostgreSQL']
                                                ['connection_string'])
        self._db_context = self._db_context_factory.create()

    def get(self):
        data = [self._resource.get_self_link(entity=entity)
                for entity
                in self._db_context.query(self._model).all()]

        links = {
            'self': app.api.url_for(self._resource_collection, _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

    def post(self):
        entity = self._model(**flask.request.get_json())

        self._db_context.add(entity, created_by=192)
        self._db_context.commit()
        self._db_context.close()

        return self._resource.to_json(entity=entity)

