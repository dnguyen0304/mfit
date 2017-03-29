# -*- coding: utf-8 -*-

from __future__ import print_function

import mfit


def handler(event, context):

    results = mfit.get_all_from_today()
    for result in results:
        print(result)
