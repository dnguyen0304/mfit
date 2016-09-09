# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class Workouts(resources.Base):

    def get(self, workout_id):
        try:
            workout = self._db_context.query(models.Workouts) \
                                       .filter_by(workout_id=workout_id) \
                                       .one()
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return Workouts.to_json(workout=workout)

    def patch(self, workout_id):
        workout = self._db_context.query(models.Workouts) \
                                   .filter_by(workout_id=workout_id) \
                                   .one()

        for attribute, value in flask.request.get_json().items():
            setattr(workout, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(workout, updated_by=999)
        self._db_context.commit()

        body = Workouts.to_json(workout=workout)

        self._db_context.close()

        return body

    def delete(self, workout_id):
        self._db_context.query(models.Workouts) \
                        .filter_by(workout_id=workout_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(workout):
        self_link = services.api.url_for(Workouts,
                                         workout_id=workout.workout_id,
                                         _external=True)
        return self_link

    @staticmethod
    def to_json(workout):
        links = {
            'self': Workouts.get_self_link(workout=workout)
        }

        data = {
            'type': 'workouts',
            'id': str(workout.workout_id),
            'attributes': workout.to_json()
        }

        body = collections.OrderedDict([('links', links), ('data', data)])

        return body

