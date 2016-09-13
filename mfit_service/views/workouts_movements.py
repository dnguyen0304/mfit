# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit_service import views


class WorkoutsMovements(views.Base):

    id = fields.Integer(attribute='workout_movement_id')
    workout = fields.Nested(views.Workouts)
    movement = fields.Nested(views.Movements)
    sets = fields.Integer()
    value = fields.Integer()
    unit = fields.Nested(views.WorkoutsMovementsUnits,
                         attribute='workout_movement_unit')
    sort_order = fields.Integer()

