# -*- coding: utf-8 -*-

import collections

import marshmallow
from marshmallow import fields

from mfit_service import resources
from mfit_service import services
from mfit_service import views


class Users(views.Base):

    id = fields.Integer(attribute='user_id')
    email_address = fields.Email()
    first_name = fields.String()
    last_name = fields.String()

    relationships = fields.Dict()

    @marshmallow.pre_dump
    def preprocess_relationships(self, entity):
        workouts_uri = services.api.url_for(
            resources.UsersWorkoutsRelationship,
            user_id=entity.user_id,
            _external=True)
        entity.relationships = collections.OrderedDict()
        entity.relationships['workouts_uri'] = workouts_uri
        return entity

