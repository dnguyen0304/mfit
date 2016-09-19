# -*- coding: utf-8 -*-

import collections

from mfit_service import resources
from mfit_service import services


class Root(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(Root, _external=True)
        }

        relationships = {
            'users_uri': services.api.url_for(resources.UsersCollection, _external=True),
            'workouts_uri': services.api.url_for(resources.WorkoutsCollection, _external=True),
            'movements_uri': services.api.url_for(resources.MovementsCollection, _external=True)}

        body = collections.OrderedDict([('relationships', relationships),
                                        ('links', links)])

        return body

