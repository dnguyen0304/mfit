# -*- coding: utf-8 -*-

import sys

from mfit import utilities

# See the StackOverflow question "How do I check if code is being run from a
# nose-test?"
# Reference: http://stackoverflow.com/a/34598987/6754214
if 'nose' not in sys.modules.keys():
    configuration = utilities.get_configuration(project_name=__name__,
                                                depth=1)

__all__ = ['configuration']

