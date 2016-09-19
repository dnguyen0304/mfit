# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class Registrations(views.Base):

    id = fields.Integer(attribute='user_workout_id')
    started_on = fields.DateTime()
    ends_on = fields.DateTime()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['logs_uri'] = resources.RegistrationsLogsCollection.get_self_link(
            registration=entity)
        entity.relationships['users_uri'] = resources.Users.get_self_link(
            user=entity.user)
        entity.relationships['workouts_uri'] = resources.Workouts.get_self_link(
            workout=entity.workout)
        return entity

