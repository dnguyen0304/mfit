# -*- coding: utf-8 -*-

import collections

import flask

from mfit import app
from mfit import models
from mfit import resources


class UsersCollection(resources.Base):

    def get(self):
        uris = [resources.Users.get_self_link(user=user)
                for user
                in self._db_context.query(models.Users).all()]

        links = {
            'self': app.api.url_for(UsersCollection, _external=True)
        }

        return collections.OrderedDict([('uris', uris),
                                        ('links', links)])

    def post(self):
        user = models.Users(**flask.request.get_json())

        self._db_context.add(user, created_by=192)
        self._db_context.commit()
        self._db_context.close()

        return resources.Users.to_json(user=user)

