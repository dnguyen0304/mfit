# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit import resources
from mfit import views


class Routines(views.Base):

    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.String(attribute='unit_name')
    sort_order = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_unit(self, routine):
        routine.unit_name = routine.routines_unit.name
        return routine

    @marshmallow.pre_dump
    def preprocess_relationships(self, routine):
        routine.relationships = collections.OrderedDict()
        routine.relationships['habit_group'] = resources.HabitGroups.get_self_link(
            entity=routine.habit_group)
        routine.relationships['habit'] = resources.Habits.get_self_link(
            entity=routine.habit)
        return routine

