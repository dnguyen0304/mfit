# -*- coding: utf-8 -*-

import io
import os

from nose.tools import (assert_equal,
                        assert_raises_regexp,
                        raises,
                        with_setup)

from mfit import utilities

__all__ = ['do_teardown',
           'test_get_configuration',
           'test_get_configuration_invalid_environment',
           'test_get_configuration_invalid_schema',
           'test_get_configuration_missing_environment',
           'test_get_configuration_standardize_project_name']


def do_teardown():

    del os.environ['FOO_ENVIRONMENT']


@with_setup(teardown=do_teardown)
def test_get_configuration():

    os.environ['FOO_ENVIRONMENT'] = 'Testing'
    _configuration_file = io.StringIO("""
{
  "Testing": {
    "foo": "bar"
  }
}
""")

    configuration = utilities.get_configuration(
        project_name='foo',
        depth=0,
        _configuration_file=_configuration_file)

    assert_equal(configuration['foo'], 'bar')


def test_get_configuration_standardize_project_name():

    with assert_raises_regexp(EnvironmentError, 'FOOBAR'):
        utilities.get_configuration(project_name='foo_bar', depth=0)


@raises(EnvironmentError)
def test_get_configuration_missing_environment():

    utilities.get_configuration(project_name='foo', depth=0)


@with_setup(teardown=do_teardown)
@raises(EnvironmentError)
def test_get_configuration_invalid_environment():

    os.environ['FOO_ENVIRONMENT'] = 'Test'
    utilities.get_configuration(project_name='foo', depth=0)


@with_setup(teardown=do_teardown)
@raises(KeyError)
def test_get_configuration_invalid_schema():

    os.environ['FOO_ENVIRONMENT'] = 'Testing'
    _configuration_file = io.StringIO("""
{
  "Foo": {
    "eggs": "ham"
  }
}
""")

    utilities.get_configuration(project_name='foo',
                                depth=0,
                                _configuration_file=_configuration_file)

