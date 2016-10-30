# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class RegistrationsLogs(views.Base):

    id = fields.Integer(attribute='user_workout_movement_id')
    sets_remaining = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['movements_uri'] = resources.Movements.get_self_link(
            movement=entity.movement)
        entity.relationships['registrations_uri'] = resources.Registrations.get_self_link(
            registration=entity.user_workout)
        return entity

