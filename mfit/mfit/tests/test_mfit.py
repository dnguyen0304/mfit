# -*- coding: utf-8 -*-

import logging

from nose.tools import assert_in, assert_is

from mfit import utilities

__all__ = ['test_package_logger_exists', 'test_global_logger_class']


def test_global_logger_class():

    assert_is(logging.getLoggerClass(), utilities.UnstructuredDataLogger)


def test_package_logger_exists():

    assert_in('mfit', logging.Logger.manager.loggerDict)

