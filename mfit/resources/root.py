# -*- coding: utf-8 -*-

import collections

from mfit import app
from mfit import resources


class Root(resources._Base):

    def get(self):
        links = {
            'self': app.api.url_for(Root, _external=True)
        }

        relationships = {
            'users_uri': app.api.url_for(resources.UsersCollection, _external=True)
        }

        body = collections.OrderedDict([('relationships', relationships),
                                        ('links', links)])

        return body

