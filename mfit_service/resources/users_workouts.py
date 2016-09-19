# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class UsersWorkouts(resources.Base):

    def get(self, user_id, user_workout_id):
        try:
            user_workout = (
                self._db_context.query(models.UsersWorkouts)
                                .filter_by(user_workout_id=user_workout_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return UsersWorkouts.to_json(user_workout=user_workout)

    def patch(self, user_id, user_workout_id):
        user_workout = (
            self._db_context.query(models.UsersWorkouts)
                            .filter_by(user_workout_id=user_workout_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(user_workout, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(user_workout, updated_by=999)
        self._db_context.commit()

        body = UsersWorkouts.to_json(user_workout=user_workout)

        self._db_context.close()

        return body

    def delete(self, user_id, user_workout_id):
        self._db_context.query(models.UsersWorkouts) \
                        .filter_by(user_workout_id=user_workout_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(user_workout):
        self_link = services.api.url_for(
            UsersWorkouts,
            user_id=user_workout.user_id,
            user_workout_id=user_workout.user_workout_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(user_workout):
        links = {
            'self': UsersWorkouts.get_self_link(user_workout=user_workout)
        }

        body = views.UsersWorkouts().dump(user_workout).data
        body.update({'links': links})

        return body

