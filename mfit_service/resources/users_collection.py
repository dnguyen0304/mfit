# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class UsersCollection(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(UsersCollection, _external=True)
        }

        users_uris = [resources.Users.get_self_link(user=user)
                      for user
                      in self._db_context.query(models.Users).all()]

        body = collections.OrderedDict([('users_uris', users_uris),
                                        ('links', links)])

        return body

    def post(self):
        user = models.Users(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(user, created_by=999)
        self._db_context.commit()

        body = resources.Users.to_json(user=user)

        self._db_context.close()

        return body

