# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views

__all__ = ['HabitGroups']


class HabitGroups(views.Base):

    name = fields.String()

