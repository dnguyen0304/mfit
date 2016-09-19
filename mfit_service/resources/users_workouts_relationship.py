# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class UsersWorkoutsRelationship(resources.Base):

    def get(self, user_id):
        links = {
            'self': services.api.url_for(UsersWorkoutsRelationship,
                                         user_id=user_id,
                                         _external=True)
        }

        users_workouts = self._db_context.query(models.UsersWorkouts) \
                                         .filter_by(user_id=user_id) \
                                         .all()

        users_workouts_uris = [
            resources.UsersWorkouts.get_self_link(user_workout=user_workout)
            for user_workout
            in users_workouts]

        body = collections.OrderedDict([('workouts_uris', users_workouts_uris),
                                        ('links', links)])

        return body

    def post(self):
        user_workout = models.UsersWorkouts(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(user_workout, created_by=999)
        self._db_context.commit()

        body = resources.UsersWorkouts.to_json(user_workout=user_workout)

        self._db_context.close()

        return body

