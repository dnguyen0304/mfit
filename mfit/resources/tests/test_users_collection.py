# -*- coding: utf-8 -*-

import http
import uuid

import requests
from nose.tools import assert_equal, assert_is_instance

from mfit.resources.tests import Base


class TestUsersCollection(Base):

    def __init__(self):
        self.self_url = ''
        self.user = {
            'email_address': 'bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            'first_name': 'Bruiser',
            'last_name': 'Nguyen'
        }

    @property
    def endpoint_name(self):
        return 'users'

    def test_get_id_type(self):
        self.self_url = requests.post(url=self.url,
                                      headers=self.headers,
                                      json=self.user).json()['links']['self']
        response = requests.get(url=self.self_url, headers=self.headers)

        assert_is_instance(response.json()['data']['id'], str)

    def test_post(self):
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.user)
        self.self_url = response.json()['links']['self']

        assert_equal(response.status_code, http.HTTPStatus.CREATED)

    def test_get_nonexistent_resource(self):
        response = requests.get(url=self.url + 'foo', headers=self.headers)
        assert_equal(response.status_code, 404)

    def test_delete_nonexistent_resource(self):
        response = requests.delete(url=self.url + 'foo', headers=self.headers)
        assert_equal(response.status_code, 404)

    def teardown(self):
        if self.self_url:
            requests.delete(url=self.self_url, headers=self.headers)

