# -*- coding: utf-8 -*-

from marshmallow import fields

from . import Base, Habits

__all__ = ['AttemptsLogs']


class AttemptsLogs(Base):

    habit = fields.Nested(Habits)

    sets_remaining = fields.Integer()

