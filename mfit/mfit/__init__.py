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
from . import enumerations
from . import models

__all__ = ['configuration', 'enumerations', 'models', 'protos']


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

    # 1. Create a new event object.
    event = models.Event(topic=enumerations.EventTopic.LOG_ADDED)
    event.arguments.attemptId = 1
    event.arguments.habitId = habit_id
    event.arguments.value = value
    event.arguments.createdBy = 1

    # 2. Serialize the new event object and add it to the queue.
    redis_client.rpush('event:all', event.to_string())

    # 3. Get the newest event from the queue and deserialize it.
    event = models.Event.from_string(redis_client.lindex('event:all', -1))

    # 4. Handle the event.
    key = 'attempt:{}:summary'.format(event.arguments.attemptId)

    # Incrementing a value does not reset it's key's expiration
    # timeout.
    time_to_live = redis_client.ttl(key)
    redis_client.hincrbyfloat(key,
                              event.arguments.habitId,
                              event.arguments.value)
    if time_to_live < 0:
        timezone = pytz.timezone('America/New_York')
        timestamp = _get_tomorrow_in_seconds(timezone=timezone)
        redis_client.expireat(key, int(timestamp))


def _get_tomorrow(timezone):

    """
    Get the start of tomorrow.

    The datetime is computed with respect to the specified timezone
    and returned converted into UTC.

    Parameters
    ----------
    timezone : pytz.tzinfo.DstTzInfo subclass

    Returns
    -------
    datetime.datetime
    """

    now = (datetime.datetime.utcnow()
                            .replace(tzinfo=pytz.utc)
                            .astimezone(tz=timezone))
    offset = now + datetime.timedelta(days=1)

    # The implementation of tzinfo in pytz differs from that of the
    # standard library. With a couple exceptions, you should therefore
    # be using the localize method instead of the tzinfo parameter.
    tomorrow_start_naive = datetime.datetime(year=offset.year,
                                             month=offset.month,
                                             day=offset.day)
    tomorrow_start = timezone.localize(dt=tomorrow_start_naive)

    return tomorrow_start.astimezone(tz=pytz.utc)


def _get_tomorrow_in_seconds(timezone):

    """
    Get the start of tomorrow in seconds (i.e. as a Unix timestamp).

    Parameters
    ----------
    timezone : pytz.tzinfo.DstTzInfo subclass

    Returns
    -------
    float
    """

    epoch = datetime.datetime(year=1970, month=1, day=1, tzinfo=pytz.utc)
    tomorrow_start = _get_tomorrow(timezone=timezone)
    seconds = (tomorrow_start - epoch).total_seconds()

    return seconds


def get_all_from_today():

    redis_client = redis.StrictRedis(host=configuration['redis']['hostname'],
                                     port=configuration['redis']['port'])

    summary = redis_client.hgetall('attempt:1:summary')

    return summary
