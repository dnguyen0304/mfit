# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit import resources
from mfit import views

__all__ = ['Attempts']


class Attempts(views.Base):

    starts_at = fields.DateTime()
    ends_at = fields.DateTime()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, attempt):
        attempt.relationships = collections.OrderedDict()
        attempt.relationships['user'] = resources.Users.get_self_url(
            entity=attempt.user)
        attempt.relationships['habit_group'] = resources.HabitGroups.get_self_url(
            entity=attempt.habit_group)
        attempt.relationships['logs'] = resources.AttemptsLogsCollection.get_self_url(
            entity=attempt)
        return attempt

