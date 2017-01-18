# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views


class Habits(views.Base):

    name = fields.String()

