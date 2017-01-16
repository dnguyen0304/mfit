# -*- coding: utf-8 -*-

import collections

import flask

from mfit import app
from mfit import models
from mfit import resources


class UsersCollection(resources.BaseCollection):

    def get(self):
        data = [resources.Users.get_self_link(entity=user)
                for user
                in self._db_context.query(models.Users).all()]

        links = {
            'self': app.api.url_for(UsersCollection, _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

    def post(self):
        user = models.Users(**flask.request.get_json())

        self._db_context.add(user, created_by=192)
        self._db_context.commit()
        self._db_context.close()

        return resources.Users.to_json(entity=user)

