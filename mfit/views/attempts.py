# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from . import Base, HabitGroups, Users

__all__ = ['Attempts']


class Attempts(Base):

    habit_group = fields.Nested(HabitGroups)
    user = fields.Nested(Users)

    starts_at = fields.DateTime()
    ends_at = fields.DateTime()

    subresources = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, attempt):
        attempt.subresources = collections.OrderedDict()
        # TODO (duyn): Return the sub-resource URL.
        attempt.subresources['logs'] = 'Not Currently Supported'
        return attempt

