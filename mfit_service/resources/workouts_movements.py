# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class WorkoutsMovements(resources.Base):

    def get(self, workout_id, workout_movement_id):
        try:
            workout_movement = (
                self._db_context.query(models.WorkoutsMovements)
                                .filter_by(workout_movement_id=workout_movement_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return WorkoutsMovements.to_json(workout_movement=workout_movement)

    def patch(self, workout_id, workout_movement_id):
        workout_movement = (
            self._db_context.query(models.WorkoutsMovements)
                            .filter_by(workout_movement_id=workout_movement_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(workout_movement, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(workout_movement, updated_by=999)
        self._db_context.commit()

        body = WorkoutsMovements.to_json(workout_movement=workout_movement)

        self._db_context.close()

        return body

    def delete(self, workout_id, workout_movement_id):
        self._db_context.query(models.WorkoutsMovements) \
                        .filter_by(workout_movement_id=workout_movement_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(workout_movement):
        self_link = services.api.url_for(
            WorkoutsMovements,
            workout_id=workout_movement.workout_id,
            workout_movement_id=workout_movement.workout_movement_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(workout_movement):
        links = {
            'self': WorkoutsMovements.get_self_link(workout_movement=workout_movement)
        }

        body = views.WorkoutsMovements().dump(workout_movement).data
        body.update({'links': links})

        return body

