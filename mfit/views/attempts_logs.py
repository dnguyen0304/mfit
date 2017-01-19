# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views

__all__ = ['AttemptsLogs']


class AttemptsLogs(views.Base):

    habit = fields.Nested(views.Habits)

    sets_remaining = fields.Integer()

