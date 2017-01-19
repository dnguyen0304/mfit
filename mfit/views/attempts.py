# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit import resources
from mfit import views

__all__ = ['Attempts']


class Attempts(views.Base):

    habit_group = fields.Nested(views.HabitGroups)
    user = fields.Nested(views.Users)

    starts_at = fields.DateTime()
    ends_at = fields.DateTime()

    subresources = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, attempt):
        attempt.subresources = collections.OrderedDict()
        attempt.subresources['logs'] = resources.AttemptsLogsCollection.get_self_url(
            entity=attempt)
        return attempt

