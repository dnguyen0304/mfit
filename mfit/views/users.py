# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views


class Users(views.Base):

    id = fields.String()
    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()

