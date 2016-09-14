# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit_service import views


class Movements(views.Base):

    id = fields.Integer(attribute='movement_id')
    name = fields.String()

