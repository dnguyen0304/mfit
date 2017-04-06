# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import site

site.addsitedir('.')

import mfit


def log_get_summary(event, context):

    results = mfit.get_all_from_today()
    for result in sorted(results.items()):
        print(result)
