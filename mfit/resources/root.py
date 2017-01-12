# -*- coding: utf-8 -*-

import collections

from mfit import app
from mfit import resources


class Root(resources.Base):

    def get(self):
        links = {
            'self': app.api.url_for(Root, _external=True)
        }

        relationships = {}

        body = collections.OrderedDict([('relationships', relationships),
                                        ('links', links)])

        return body

