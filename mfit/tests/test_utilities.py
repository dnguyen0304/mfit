# -*- coding: utf-8 -*-

import io
import os

from nose.tools import (assert_equal,
                        assert_raises,
                        assert_raises_regexp,
                        assert_true,
                        raises,
                        with_setup)

from mfit import utilities

__all__ = ['TestContextFilter',
           'do_teardown',
           'test_get_configuration',
           'test_get_configuration_invalid_environment',
           'test_get_configuration_invalid_schema',
           'test_get_configuration_missing_environment',
           'test_get_configuration_standardize_application_name']


class TestContextFilter:

    def setup(self):
        class LogRecord:
            pass
        self.context_filter = utilities.ContextFilter(application_name='foo')
        self.log_record = LogRecord()

    def test_has_event_id(self):
        with assert_raises(AttributeError):
            self.log_record.event_id
        self.context_filter.filter(log_record=self.log_record)

        assert_true(self.log_record.event_id)

    def test_has_process_name(self):
        with assert_raises(AttributeError):
            self.log_record.process_name
        self.context_filter.filter(log_record=self.log_record)

        assert_equal(self.log_record.process_name, 'foo')


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
        application_name='foo',
        _configuration_file=_configuration_file)

    assert_equal(configuration['foo'], 'bar')


def test_get_configuration_standardize_application_name():

    with assert_raises_regexp(EnvironmentError, 'FOOBAR'):
        utilities.get_configuration(application_name='foo_bar')


@raises(EnvironmentError)
def test_get_configuration_missing_environment():

    utilities.get_configuration(application_name='foo')


@with_setup(teardown=do_teardown)
@raises(EnvironmentError)
def test_get_configuration_missing_configuration_file_path():

    os.environ['FOO_ENVIRONMENT'] = 'Testing'
    utilities.get_configuration(application_name='foo')


@with_setup(teardown=do_teardown)
@raises(EnvironmentError)
def test_get_configuration_invalid_environment():

    os.environ['FOO_ENVIRONMENT'] = 'Test'
    utilities.get_configuration(application_name='foo')


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

    utilities.get_configuration(application_name='foo',
                                _configuration_file=_configuration_file)

