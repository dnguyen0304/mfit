# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class UsersWorkoutsLogsCollection(resources.Base):

    def get(self, user_id, user_workout_id):
        links = {
            'self': self.get_self_link(user_id=user_id,
                                       user_workout_id=user_workout_id)
        }

        users_workouts_logs = self._db_context.query(models.UsersWorkoutsMovements) \
                                              .filter_by(user_workout_id=user_workout_id) \
                                              .all()

        users_workouts_logs_uris = [
            resources.UsersWorkoutsLogs.get_self_link(user_workout_log=user_workout_log)
            for user_workout_log
            in users_workouts_logs]

        body = collections.OrderedDict([('logs_uris', users_workouts_logs_uris),
                                        ('links', links)])

        return body

    def post(self):
        user_workout_log = models.UsersWorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(user_workout_log, created_by=999)
        self._db_context.commit()

        body = resources.UsersWorkoutsLogs.to_json(user_workout_log=user_workout_log)

        self._db_context.close()

        return body

    @classmethod
    def get_self_link(cls, user_id, user_workout_id):
        self_link = services.api.url_for(cls,
                                         user_id=user_id,
                                         user_workout_id=user_workout_id,
                                         _external=True)
        return self_link

