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
        movements_uri = services.api.url_for(
            resources.WorkoutsMovementsRelationships,
            workout_id=entity.workout_id,
            _external=True)
        entity.relationships = collections.OrderedDict()
        entity.relationships['movements_uri'] = movements_uri
        return entity
