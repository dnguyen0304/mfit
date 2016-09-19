# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class UsersWorkoutsLogs(views.Base):

    id = fields.Integer(attribute='user_workout_movement_id')
    sets_remaining = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['workouts_uri'] = resources.Registrations.get_self_link(
            user_workout=entity.user_workout)
        entity.relationships['movements_uri'] = resources.Movements.get_self_link(
            movement=entity.movement)
        return entity

