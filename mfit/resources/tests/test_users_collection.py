# -*- coding: utf-8 -*-

import uuid

import requests
from nose.tools import assert_equal

from mfit.resources.tests import Base


class TestUsersCollection(Base):

    def __init__(self):
        self.user = {
            'email_address': 'bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            'first_name': 'Bruiser',
            'last_name': 'Nguyen'
        }

    @property
    def endpoint_name(self):
        return 'users'

    def test_get_nonexistent_resource(self):
        response = requests.get(url=self.url + 'foo', headers=self.headers)
        assert_equal(response.status_code, 404)

    def test_delete_nonexistent_resource(self):
        self_url = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.user).json()['links']['self']
        requests.delete(url=self_url, headers=self.headers, json=self.user)

        response = requests.delete(url=self_url,
                                   headers=self.headers,
                                   json=self.user)

        assert_equal(response.status_code, 404)

