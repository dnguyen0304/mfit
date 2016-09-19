# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class Registrations(resources.Base):

    def get(self, registration_id):
        try:
            registration = (
                self._db_context.query(models.UsersWorkouts)
                                .filter_by(user_workout_id=registration_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return Registrations.to_json(registration=registration)

    def patch(self, registration_id):
        registration = (
            self._db_context.query(models.UsersWorkouts)
                            .filter_by(user_workout_id=registration_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(registration, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(registration, updated_by=999)
        self._db_context.commit()

        body = Registrations.to_json(registration=registration)

        self._db_context.close()

        return body

    def delete(self, registration_id):
        self._db_context.query(models.UsersWorkouts) \
                        .filter_by(user_workout_id=registration_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(registration):
        self_link = services.api.url_for(
            Registrations,
            registration_id=registration.user_workout_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(registration):
        links = {
            'self': Registrations.get_self_link(registration=registration)
        }

        body = views.Registrations().dump(registration).data
        body.update({'links': links})

        return body

