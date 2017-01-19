# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit import resources
from mfit import views

__all__ = ['AttemptsLogs']


class AttemptsLogs(views.Base):

    sets_remaining = fields.Integer()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, attempt_log):
        attempt_log.relationships = collections.OrderedDict()
        attempt_log.relationships['habit'] = resources.Habits.get_self_url(
            entity=attempt_log.habit)
        return attempt_log

