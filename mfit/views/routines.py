# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields

from mfit import views

__all__ = ['Routines']


class Routines(views.Base):

    habit = fields.Nested(views.Habits)
    habit_group = fields.Nested(views.HabitGroups)

    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.String(attribute='unit_name')
    sort_order = fields.Integer()

    @marshmallow.pre_dump
    def preprocess_unit(self, routine):
        routine.unit_name = routine.routines_unit.name
        return routine

