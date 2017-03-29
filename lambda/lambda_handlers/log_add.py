# -*- coding: utf-8 -*-

import mfit


def handler(event, context):

    mfit.add(habit_id=event['habit_id'], value=event['value'])
