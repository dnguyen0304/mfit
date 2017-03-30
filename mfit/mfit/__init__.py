# -*- coding: utf-8 -*-

import datetime
import functools
import itertools
import json
import logging.config
import os

import dateutil.parser
import pytz
import redis

from . import protos

__all__ = ['configuration', 'protos']


def get_configuration(application_name):

    configuration_file_path = os.environ[
        application_name.upper() + '_CONFIGURATION_FILE_PATH']

    with open(configuration_file_path, 'r') as file:
        parsed_configuration = json.loads(file.read())

    return parsed_configuration


configuration = get_configuration(application_name=__name__)
logging.config.dictConfig(config=configuration['logging'])


def add(habit_id, value):

    redis_client = redis.StrictRedis(host=configuration['redis']['hostname'],
                                     port=configuration['redis']['port'])

    next_log_id = redis_client.get('log:id:next')

    now = datetime.datetime.utcnow()
    now.replace(tzinfo=pytz.utc)

    log = {'log_id': next_log_id,
           'attempt_id': 1,
           'habit_id': habit_id,
           'value': value,
           'created_at': now.isoformat(),
           'created_by': 1,
           'updated_at': None,
           'updated_by': None}

    redis_client.rpush('log:all', json.dumps(log))

    redis_client.incr('log:id:next')


def get_all_from_today():

    redis_client = redis.StrictRedis(host=configuration['redis']['hostname'],
                                     port=configuration['redis']['port'])

    now = datetime.datetime.utcnow()
    now.replace(tzinfo=pytz.utc)

    results = [json.loads(result)
               for result
               in redis_client.lrange('log:all', 0, -1)]
    for result in results:
        result['created_at'] = dateutil.parser.parse(result['created_at'])

    # The groupby function in Python expects input values to be sorted.
    # Note this behavior differs from the GROUP BY clause in SQL. When
    # performing nested operations, sort on the innermost key first.
    sorted_results = sorted(results,
                            key=lambda x: (x['habit_id'], x['created_at']))

    # The returned groups are implemented as shared iterators. This
    # intermediary step is therefore necessary when performing nested
    # operations.
    grouped_results = [
        [key, list(group)]
        for key, group
        in itertools.groupby(iterable=sorted_results,
                             key=lambda x: (x['created_at'].date(), x['habit_id']))]
    for grouped_result in grouped_results:
        grouped_result[1] = functools.reduce(lambda x, y: x + int(y['value']),
                                             grouped_result[1],
                                             0)
    return grouped_results
