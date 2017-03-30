# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import site

site.addsitedir('.')

import mfit


def handler(event, context):

    mfit.add(habit_id=event['habit_id'], value=event['value'])
    results = mfit.get_all_from_today()
    for result in results:
        print(result)
