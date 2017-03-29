# -*- coding: utf-8 -*-

from mfit.resources.tests import RootBase

__all__ = ['TestRoot']


class TestRoot(RootBase):

    @property
    def endpoint_name(self):
        return 'root'

