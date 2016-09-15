# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import services
from mfit_service import views


class Workouts(views.Base):

    id = fields.Integer(attribute='workout_id')
    name = fields.String()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        programs_uri = services.api.url_for(
            resources.WorkoutsProgramsRelationship,
            workout_id=entity.workout_id,
            _external=True)
        entity.relationships = collections.OrderedDict()
        entity.relationships['programs_uri'] = programs_uri
        return entity
