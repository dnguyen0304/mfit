# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit_service import views


class Users(views.Base):

    id = fields.Integer(attribute='user_id')
    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()

