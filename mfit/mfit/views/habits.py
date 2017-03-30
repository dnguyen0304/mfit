# -*- coding: utf-8 -*-

from marshmallow import fields

from . import Base

__all__ = ['Habits']


class Habits(Base):

    name = fields.String()

