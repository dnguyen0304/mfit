# -*- coding: utf-8 -*-

from marshmallow import fields

from . import Base

__all__ = ['Users']


class Users(Base):

    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()

