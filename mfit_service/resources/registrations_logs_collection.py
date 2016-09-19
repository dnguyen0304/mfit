# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class RegistrationsLogsCollection(resources.Base):

    def get(self, registration_id):
        registration = (
            self._db_context.query(models.UsersWorkouts)
                            .filter_by(user_workout_id=registration_id)
                            .one())
        registrations_logs = registration.movements

        links = {'self': self.get_self_link(registration=registration)}

        registrations_logs_uris = [
            resources.RegistrationsLogs.get_self_link(registration_log=registration_log)
            for registration_log
            in registrations_logs]

        body = collections.OrderedDict([('logs_uris', registrations_logs_uris),
                                        ('links', links)])

        return body

    def post(self):
        registration_log = models.UsersWorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(registration_log, created_by=999)
        self._db_context.commit()

        body = resources.RegistrationsLogs.to_json(registration_log=registration_log)

        self._db_context.close()

        return body

    @classmethod
    def get_self_link(cls, registration):
        self_link = services.api.url_for(
            cls,
            registration_id=registration.user_workout_id,
            _external=True)
        return self_link

