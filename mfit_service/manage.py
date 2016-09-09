"""
See the answer submitted by dbw for more details.

Related Links
-------------
1. http://stackoverflow.com/a/13888865
"""

import copy
import sys

import nose

from mfit_service.services.tests import test_db_context


def run_test_suite():
    test_registry = [test_db_context]

    sys_argv = copy.copy(sys.argv)
    sys_argv.remove('test')

    for test in test_registry:
        argv = ['_', test.__name__]
        argv.extend(sys_argv[1:])
        nose.run(argv=argv)

