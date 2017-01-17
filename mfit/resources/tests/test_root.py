# -*- coding: utf-8 -*-

from nose.tools import nottest

from mfit.resources.tests import Base


class TestRoot(Base):

    @property
    def endpoint_name(self):
        return 'root'

    @nottest
    def test_is_discoverable(self):
        pass

