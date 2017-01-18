# -*- coding: utf-8 -*-

import argparse

from nose.tools import (assert_false,
                        assert_is_instance,
                        assert_list_equal,
                        assert_true,
                        raises)

from mfit import app


class TestArgumentParser:

    def __init__(self):
        self.argument_parser = app.get_argument_parser()

    def test_return_type(self):
        output = self.argument_parser.parse_args(args='')
        assert_is_instance(output, tuple)
        assert_is_instance(output[0], argparse.Namespace)
        assert_is_instance(output[1], list)

    def test_no_arguments(self):
        args, test_runner_args = self.argument_parser.parse_args(args='')
        assert_false(args.in_test_mode)
        assert_list_equal(test_runner_args, list())

    def test_in_test_mode(self):
        args = '--in-test-mode'.split()
        args, test_runner_args = self.argument_parser.parse_args(args=args)
        assert_true(args.in_test_mode)
        assert_list_equal(test_runner_args, list())

    def test_in_test_mode_with_test_runner_options(self):
        args = '--in-test-mode --foo'.split()
        args, test_runner_args = self.argument_parser.parse_args(args=args)
        assert_true(args.in_test_mode)
        assert_list_equal(test_runner_args, ['--foo'])

    def test_in_test_mode_with_test_runner_options_reversed_sort_order(self):
        args = '--foo --in-test-mode'.split()
        args, test_runner_args = self.argument_parser.parse_args(args=args)
        assert_true(args.in_test_mode)
        assert_list_equal(test_runner_args, ['--foo'])

    @raises(SystemExit)
    def test_test_runner_options_without_in_test_mode(self):
        args = '--foo'.split()
        self.argument_parser.parse_args(args=args)

