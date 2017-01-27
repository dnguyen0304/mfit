# -*- coding: utf-8 -*-

from marshmallow import fields

from . import Base

__all__ = ['HabitGroups']


class HabitGroups(Base):

    name = fields.String()

