# -*- coding: utf-8 -*-

import uuid

from mfit.resources.tests import Base

__all__ = ['TestHabits']


class TestHabits(Base):

    @property
    def endpoint_name(self):
        return 'habits'

    @property
    def data(self):
        return {
            # Remove hyphens to be within the acceptable length for
            # this attribute.
            'name': str(uuid.uuid4()).replace('-', '')
        }

