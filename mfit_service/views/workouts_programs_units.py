# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit_service import views


class WorkoutsProgramsUnits(views.Base):

    id = fields.Integer(attribute='workout_movement_unit_id')
    name = fields.String()

