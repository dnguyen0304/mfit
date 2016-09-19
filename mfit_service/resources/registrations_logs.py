# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class RegistrationsLogs(resources.Base):

    def get(self, registration_id, registration_log_id):
        try:
            registration_log = (
                self._db_context.query(models.UsersWorkoutsMovements)
                                .filter_by(user_workout_movement_id=registration_log_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return RegistrationsLogs.to_json(registration_log=registration_log)

    def patch(self, registration_id, registration_log_id):
        registration_log = (
            self._db_context.query(models.UsersWorkoutsMovements)
                            .filter_by(user_workout_movement_id=registration_log_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(registration_log, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(registration_log, updated_by=999)
        self._db_context.commit()

        body = RegistrationsLogs.to_json(registration_log=registration_log)

        self._db_context.close()

        return body

    def delete(self, registration_id, registration_log_id):
        self._db_context.query(models.UsersWorkoutsMovements) \
                        .filter_by(user_workout_movement_id=registration_log_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(registration_log):
        self_link = services.api.url_for(
            RegistrationsLogs,
            registration_id=registration_log.user_workout.user_workout_id,
            registration_log_id=registration_log.user_workout_movement_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(registration_log):
        links = {
            'self': RegistrationsLogs.get_self_link(registration_log=registration_log)
        }

        body = views.RegistrationsLogs().dump(registration_log).data
        body.update({'links': links})

        return body

