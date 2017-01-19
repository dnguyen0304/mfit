# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views

__all__ = ['Habits']


class Habits(views.Base):

    name = fields.String()

