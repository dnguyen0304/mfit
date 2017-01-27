# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields

from . import Base, HabitGroups, Habits

__all__ = ['Routines']


class Routines(Base):

    habit = fields.Nested(Habits)
    habit_group = fields.Nested(HabitGroups)

    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.String(attribute='unit_name')
    sort_order = fields.Integer()

    @marshmallow.pre_dump
    def preprocess_unit(self, routine):
        routine.unit_name = routine.routines_unit.name
        return routine

