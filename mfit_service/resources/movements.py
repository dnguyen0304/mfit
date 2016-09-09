# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class Movements(resources.Base):

    def get(self, movement_id):
        try:
            movement = self._db_context.query(models.Movements) \
                                       .filter_by(movement_id=movement_id) \
                                       .one()
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return Movements.to_json(movement=movement)

    def patch(self, movement_id):
        movement = self._db_context.query(models.Movements) \
                                   .filter_by(movement_id=movement_id) \
                                   .one()

        for attribute, value in flask.request.get_json().items():
            setattr(movement, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(movement, updated_by=999)
        self._db_context.commit()

        body = Movements.to_json(movement=movement)

        self._db_context.close()

        return body

    def delete(self, movement_id):
        self._db_context.query(models.Movements) \
                        .filter_by(movement_id=movement_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(movement):
        self_link = services.api.url_for(Movements,
                                         movement_id=movement.movement_id,
                                         _external=True)
        return self_link

    @staticmethod
    def to_json(movement):
        links = {
            'self': Movements.get_self_link(movement=movement)
        }

        data = {
            'type': 'movements',
            'id': str(movement.movement_id),
            'attributes': movement.to_json()
        }

        body = collections.OrderedDict([('links', links), ('data', data)])

        return body

