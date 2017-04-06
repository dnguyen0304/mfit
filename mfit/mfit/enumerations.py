# -*- coding: utf-8 -*-

from . import protos


class EventTopic(object):
    pass


def construct_enumeration(enumeration, mappings):

    for mapping in mappings:
        setattr(enumeration, *mapping)


construct_enumeration(EventTopic, protos.Event.Topic.items())
