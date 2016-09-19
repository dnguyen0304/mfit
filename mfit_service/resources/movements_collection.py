# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class MovementsCollection(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(MovementsCollection, _external=True)
        }

        movements_uris = [resources.Movements.get_self_link(movement=movement)
                          for movement
                          in self._db_context.query(models.Movements).all()]

        body = collections.OrderedDict([('movements_uris', movements_uris),
                                        ('links', links)])

        return body

    def post(self):
        movement = models.Movements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(movement, created_by=999)
        self._db_context.commit()

        body = resources.Movements.to_json(movement=movement)

        self._db_context.close()

        return body

