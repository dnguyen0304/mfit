# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class UsersWorkoutsLogs(resources.Base):

    def get(self, user_id, user_workout_id, user_workout_log_id):
        try:
            user_workout_log = (
                self._db_context.query(models.UsersWorkoutsMovements)
                                .filter_by(user_workout_movement_id=user_workout_log_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return UsersWorkoutsLogs.to_json(user_workout_log=user_workout_log)

    def patch(self, user_id, user_workout_id, user_workout_log_id):
        user_workout_log = (
            self._db_context.query(models.UsersWorkoutsMovements)
                            .filter_by(user_workout_movement_id=user_workout_log_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(user_workout_log, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(user_workout_log, updated_by=999)
        self._db_context.commit()

        body = UsersWorkoutsLogs.to_json(user_workout_log=user_workout_log)

        self._db_context.close()

        return body

    def delete(self, user_id, user_workout_id, user_workout_log_id):
        self._db_context.query(models.UsersWorkoutsMovements) \
                        .filter_by(user_workout_movement_id=user_workout_log_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(user_workout_log):
        self_link = services.api.url_for(
            UsersWorkoutsLogs,
            user_id=user_workout_log.user_workout.user.user_id,
            user_workout_id=user_workout_log.user_workout.user_workout_id,
            user_workout_log_id=user_workout_log.user_workout_movement_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(user_workout_log):
        links = {
            'self': UsersWorkoutsLogs.get_self_link(user_workout_log=user_workout_log)
        }

        body = views.UsersWorkoutsLogs().dump(user_workout_log).data
        body.update({'links': links})

        return body

