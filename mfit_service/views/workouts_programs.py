# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class WorkoutsPrograms(views.Base):

    id = fields.Integer(attribute='workout_movement_id')
    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.String(attribute='workout_program_unit_name')
    sort_order = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_workout_program_unit(self, entity):
        entity.workout_program_unit_name = entity.workout_movement_unit.name
        return entity

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['movement'] = resources.Movements.get_self_link(
            movement=entity.movement)
        return entity

