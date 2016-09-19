# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class RegistrationsCollection(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(RegistrationsCollection, _external=True)
        }

        registrations_uris = [
            resources.Registrations.get_self_link(registration=registration)
            for registration
            in self._db_context.query(models.UsersWorkouts).all()]

        body = collections.OrderedDict([
            ('registrations_uris', registrations_uris),
            ('links', links)])

        return body

    def post(self):
        registration = models.UsersWorkouts(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(registration, created_by=999)
        self._db_context.commit()

        body = resources.Registrations.to_json(registration=registration)

        self._db_context.close()

        return body

