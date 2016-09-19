# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import views


class UsersWorkouts(views.Base):

    id = fields.Integer(attribute='user_workout_id')
    started_on = fields.DateTime()
    ends_on = fields.DateTime()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        entity.relationships = collections.OrderedDict()
        entity.relationships['logs_uri'] = resources.UsersWorkoutsLogsCollection.get_self_link(
            user_id=entity.user.user_id,
            user_workout_id=entity.user_workout_id)
        entity.relationships['workouts_uri'] = resources.Workouts.get_self_link(
            workout=entity.workout)
        return entity

