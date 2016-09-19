# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class WorkoutsCollection(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(WorkoutsCollection, _external=True)
        }

        workouts_uris = [resources.Workouts.get_self_link(workout=workout)
                         for workout
                         in self._db_context.query(models.Workouts).all()]

        body = collections.OrderedDict([('workouts_uris', workouts_uris),
                                        ('links', links)])

        return body

    def post(self):
        workout = models.Workouts(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(workout, created_by=999)
        self._db_context.commit()

        body = resources.Workouts.to_json(workout=workout)

        self._db_context.close()

        return body

