# -*- coding: utf-8 -*-

import uuid

from nose.plugins.attrib import attr

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

    @attr('requirements.must_have')
    def test_create_new_user(self):
        self.test_post_returns_201_status_code()
        self.test_post_returns_location_header()
        self.test_post_body_has_data_not_null()
        self.test_post_body_has_self_url()

