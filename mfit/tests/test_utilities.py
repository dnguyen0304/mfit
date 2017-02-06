# -*- coding: utf-8 -*-

import io
import logging
import os

from nose import SkipTest
from nose.tools import (assert_equal,
                        assert_false,
                        assert_in,
                        assert_list_equal,
                        assert_raises,
                        assert_raises_regexp,
                        assert_true,
                        raises,
                        with_setup)

# Should this module not import the mfit package to respect the package
# hierarchy?
import mfit
from mfit import utilities

__all__ = ['TestContextFilter',
           'TestJsonFormatter',
           'TestKafkaHandler',
           'TestUnstructuredDataLogger',
           'do_teardown',
           'test_get_configuration',
           'test_get_configuration_invalid_environment',
           'test_get_configuration_invalid_schema',
           'test_get_configuration_missing_environment',
           'test_get_configuration_standardize_application_name',
           'test_format_extra_as_json']


class TestUnstructuredDataLogger:

    def test_can_identify_extra(self):
        log_record = TestUnstructuredDataLogger.get_log_record()
        assert_true(hasattr(log_record, '_extra'))

    @staticmethod
    def get_log_record(extra=None):
        logger = utilities.UnstructuredDataLogger(name='')
        log_record = logger.makeRecord(name='',
                                       level='',
                                       fn='',
                                       lno='',
                                       msg='',
                                       args='',
                                       exc_info='',
                                       extra=extra or dict())
        return log_record


class TestJsonFormatter:

    def setup(self):
        class LogRecord:
            pass

        self.formatter = utilities.JsonFormatter(fmt=logging.BASIC_FORMAT)
        self.log_record = LogRecord()

        self.log_record.levelname = 'levelname'
        self.log_record.name = 'name'
        self.log_record.message = 'message'

    def test_to_json(self):
        output = self.formatter.formatMessage(record=self.log_record)

        assert_true(output.startswith('{'))
        assert_true(output.endswith('}'))
        assert_in("'levelname': 'levelname'", output)
        assert_in("'name': 'name'", output)
        assert_in("'message': 'message'", output)

    def test_to_json_does_not_raise_attribute_error(self):
        raised_error = False
        try:
            self.formatter.formatMessage(record=self.log_record)
        except AttributeError:
            raised_error = True
        assert_false(raised_error)

    def test_parse_format(self):
        expected = ['levelname', 'name', 'message']
        output = self.formatter._parse_format(logging.BASIC_FORMAT)
        assert_list_equal(output, expected)

    def test_parse_format_no_replacement_fields(self):
        expected = list()
        output = self.formatter._parse_format('')
        assert_list_equal(output, expected)


class TestKafkaHandler:

    def setup(self):
        self.configuration = (mfit.configuration['components']
                                                ['logging']
                                                ['handlers']
                                                ['message_queue'])
        hostname = self.configuration['hostname']
        port = self.configuration['port']

        self.producer = utilities.KafkaHandler._get_producer(hostname=hostname,
                                                             port=port,
                                                             topic_name='')

    def test_get_producer_accepts_port_of_type_numeric(self):
        raised_error = False
        hostname = self.configuration['hostname']
        port = int(self.configuration['port'])

        try:
            utilities.KafkaHandler._get_producer(hostname=hostname,
                                                 port=port,
                                                 topic_name='')
        except TypeError:
            raised_error = True

        assert_false(raised_error)

    def test_get_producer_producer_has_isend_method(self):
        assert_true(hasattr(self.producer, 'isend'))

    # A proper teardown for the following test would require deleting
    # Topics. As noted below, the Kafka server does not expose an API
    # for deleting Topics [1]. Implementing this feature is
    # "non-trivial" [2].
    #
    # References
    # ----------
    # .. [1] "Topics are not deleted but lingered."
    #    https://github.com/dpkp/kafka-python/issues/363
    # .. [2] "Feature: Delete topics"
    #    https://github.com/dpkp/kafka-python/issues/433
    def test_get_producer_producer_isend_only_requires_value_parameter(self):
        raise SkipTest

    def test_get_producer_producer_serialization(self):
        expected = b'foo'
        output = self.producer.config['value_serializer']('foo')
        assert_equal(output, expected)


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


def test_format_extra_as_json():

    extra = {'foo': 'bar'}
    log_record = TestUnstructuredDataLogger.get_log_record(extra=extra)
    log_record.message = ''
    formatter = utilities.JsonFormatter()

    output = formatter.formatMessage(record=log_record)

    assert_in("'foo': 'bar'", output)


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

