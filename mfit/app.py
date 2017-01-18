#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
mFit REST API.

This is the entry point for managing the API. This package is designed
to be started as a service rather than called as an external library.
To start the service, from the terminal run

    python mfit/app.py

"""

import argparse

import mfit


class ArgumentParser(argparse.ArgumentParser):

    def parse_args(self, args=None, namespace=None):

        """
        Parse the arguments that have been passed to the command-line
        utility.

        Extends argparse.ArgumentParser.parse_args(). The standard
        library argument parser cannot handle the situation where a
        command-line utility accepts an optional flag and then
        an arbitrary number of remaining arguments (i.e.
        nargs=argparse.REMAINDER).

        Parameters
        ----------
        args : str, optional
            Defaults to None.
        namespace : argparse.Namespace, optional
            Defaults to None.

        Returns
        -------
        tuple
            Two-element tuple. The first element is a populated
            argparse.Namespace. The second element is a list of strings
            of arguments for the test runner.

        See Also
        --------
        argparse.ArgumentParser.parse_args()
        argparse.ArgumentParser.parse_known_args()
        """

        args_, test_runner_args = self.parse_known_args(args=args,
                                                        namespace=namespace)
        if not args_.in_test_mode and test_runner_args:
            args_ = super().parse_args(args=args, namespace=namespace)
        return args_, test_runner_args


def get_argument_parser():

    """
    Get a configured ArgumentParser.

    Returns
    -------
    app.ArgumentParser
    """

    in_test_mode_help = ("Run the test suite. All remaining (i.e. unmatched) "
                         "arguments are passed to the test runner. "
                         "Acceptable values are equivalent to those for the "
                         "`nose` framework.")

    parser = ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--in-test-mode',
                        dest='in_test_mode',
                        action='store_true',
                        help=in_test_mode_help)

    return parser


if __name__ == '__main__':
    argument_parser = get_argument_parser()
    args, test_runner_args = argument_parser.parse_args()

    mfit.main(in_test_mode=args.in_test_mode,
              test_runner_args=test_runner_args)

