# -*- coding: utf-8 -*-

from mfit.resources.tests import Base


class TestUsersCollection(Base):

    @property
    def endpoint_name(self):
        return 'users'

