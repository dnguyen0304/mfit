# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit_service import views


class Workouts(views.Base):

    id = fields.Integer(attribute='workout_id')
    name = fields.String()

