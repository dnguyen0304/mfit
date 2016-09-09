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

        data = []

        body = collections.OrderedDict([('links', links), ('data', data)])

        for workout in self._db_context.query(models.Workouts).all():
            self_link = resources.Workouts.get_self_link(workout=workout)
            data.append(self_link)

        return body

    def post(self):
        workout = models.Workouts(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(workout, created_by=999)
        self._db_context.commit()

        body = resources.Workouts.to_json(workout=workout)

        self._db_context.close()

        return body

