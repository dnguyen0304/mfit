# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class Programs(views.Base):

    id = fields.Integer(attribute='workout_movement_id')
    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.String(attribute='unit_name')
    sort_order = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_unit(self, entity):
        entity.unit_name = entity.workout_movement_unit.name
        return entity

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['workouts_uri'] = resources.Workouts.get_self_link(
            workout=entity.workout)
        entity.relationships['movements_uri'] = resources.Movements.get_self_link(
            movement=entity.movement)
        return entity

