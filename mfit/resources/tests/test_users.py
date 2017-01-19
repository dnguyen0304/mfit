# -*- coding: utf-8 -*-

import uuid

from mfit.resources.tests import Base

__all__ = ['TestUsers']


class TestUsers(Base):

    @property
    def endpoint_name(self):
        return 'users'

    @property
    def data(self):
        return {
            'email_address': 'bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            'first_name': 'Bruiser',
            'last_name': 'Nguyen'
        }

