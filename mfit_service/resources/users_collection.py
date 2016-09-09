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

        data = []

        body = collections.OrderedDict([('links', links), ('data', data)])

        for user in self._db_context.query(models.Users).all():
            self_link = resources.Users.get_self_link(user=user)
            data.append(self_link)

        return body

    def post(self):
        user = models.Users(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(user, created_by=999)
        self._db_context.commit()

        body = resources.Users.to_json(user=user)

        self._db_context.close()

        return body

