# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class WorkoutsMovementsRelationships(resources.Base):

    def get(self, workout_id):
        links = {
            'self': services.api.url_for(WorkoutsMovementsRelationships,
                                         workout_id=workout_id,
                                         _external=True)
        }

        workout_movement_uris = []
        body = collections.OrderedDict([('movements', workout_movement_uris),
                                        ('links', links)])
        workout_movements = self._db_context.query(models.WorkoutsMovements) \
                                            .filter_by(workout_id=workout_id) \
                                            .all()

        for workout_movement in workout_movements:
            self_link = resources.WorkoutsMovements.get_self_link(
                workout_movement=workout_movement)
            workout_movement_uris.append(self_link)

        return body

    def post(self):
        workout_movement = models.WorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(workout_movement, created_by=999)
        self._db_context.commit()

        body = resources.WorkoutsMovements.to_json(workout_movement=workout_movement)

        self._db_context.close()

        return body

