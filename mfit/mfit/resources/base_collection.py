# -*- coding: utf-8 -*-

import collections
import sys

if sys.version_info == (2, 7):
    import httplib as HttpStatusCode
elif sys.version_info >= (3, 0):
    import http.client as HttpStatusCode

import flask

import mfit
from . import _Base


__all__ = ['BaseCollection']


class BaseCollection(_Base):

    _model = None
    _resource = None
    _resource_collection = None

    def get(self):
        data = [self._resource.get_self_url(entity=entity)
                for entity
                in self._db_context.query(self._model).all()]

        urls = {
            'self': mfit.api.url_for(self._resource_collection, _external=True)
        }

        return collections.OrderedDict([('data', data), ('urls', urls)])

    def post(self):
        entity = self._model(**flask.request.get_json())

        self._db_context.add(entity, created_by=192)
        self._db_context.commit()

        body = self._resource.to_json(entity=entity)
        headers = {
            'Location': body['urls']['self']
        }

        self._db_context.close()

        return body, HttpStatusCode.CREATED, headers

