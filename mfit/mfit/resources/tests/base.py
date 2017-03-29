# -*- coding: utf-8 -*-

import abc
import sys

if sys.version_info == (2, 7):
    import httplib as HttpStatusCode
elif sys.version_info >= (3, 0):
    import http.client as HttpStatusCode

import requests
from nose.tools import (assert_equal,
                        assert_in,
                        assert_is_instance,
                        assert_true)

__all__ = ['Base', 'RootBase']


class RootBase(metaclass=abc.ABCMeta):

    api_version = 'v1'
    root_url = 'http://127.0.0.1:5000/' + api_version + '/'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    @property
    @abc.abstractmethod
    def endpoint_name(self):
        pass

    @property
    def url(self):
        url = self.root_url
        if self.endpoint_name.lower().strip() != 'root':
            url += self.endpoint_name
        if not url.endswith('/'):
            url += '/'
        return url

    def test_get_collection_returns_200_status_code(self):
        response = requests.head(url=self.url, headers=self.headers)
        assert_true(response.ok)

    def test_get_body_has_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        assert_in('data', response.json())

    def test_get_body_has_urls(self):
        response = requests.get(url=self.url, headers=self.headers)
        assert_in('urls', response.json())

    def test_get_body_has_self_url(self):
        response = requests.get(url=self.url, headers=self.headers)
        assert_equal(self.url, response.json()['urls']['self'])


class Base(RootBase):

    def __init__(self):
        # Check this attribute to determine if a teardown is necessary.
        self.self_url = ''

    @property
    @abc.abstractmethod
    def data(self):
        pass

    def test_get_subresources_are_discoverable(self):
        response = requests.get(url=self.root_url, headers=self.headers)
        discovered_url = response.json()['data']['subresources'].get(
            self.endpoint_name,
            '')
        assert_equal(discovered_url, self.url)

    def test_get_id_attribute_is_of_type_string(self):
        self.self_url = requests.post(url=self.url,
                                      headers=self.headers,
                                      json=self.data).json()['urls']['self']
        response = requests.get(url=self.self_url, headers=self.headers)

        assert_is_instance(response.json()['data']['id'], str)

    def test_get_nonexistent_resource_returns_404_status_code(self):
        response = requests.get(url=self.url + 'foo', headers=self.headers)
        assert_equal(response.status_code, HttpStatusCode.NOT_FOUND)

    def test_post_returns_201_status_code(self):
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.data)
        self.self_url = response.json()['urls']['self']

        assert_equal(response.status_code, HttpStatusCode.CREATED)

    def test_post_returns_location_header(self):
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.data)
        self.self_url = response.json()['urls']['self']

        assert_equal(response.headers['Location'], self.self_url)

    def test_post_body_has_data_not_null(self):
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.data)
        self.self_url = response.json()['urls']['self']

        assert_true(response.json()['data'])

    def test_post_body_has_self_url(self):
        response = requests.post(url=self.url,
                                 headers=self.headers,
                                 json=self.data)
        self.self_url = response.json()['urls']['self']

        assert_true(response.json()['urls']['self'])

    def test_delete_nonexistent_resource_returns_404_status_code(self):
        response = requests.delete(url=self.url + 'foo', headers=self.headers)
        assert_equal(response.status_code, HttpStatusCode.NOT_FOUND)

    def teardown(self):
        if self.self_url:
            requests.delete(url=self.self_url, headers=self.headers)

