# -*- coding: utf-8 -*-

from marshmallow import fields

from mfit import views

__all__ = ['Users']


class Users(views.Base):

    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()

