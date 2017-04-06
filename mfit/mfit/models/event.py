# -*- coding: utf-8 -*-

import datetime
import uuid

from .. import protos


class Event(object):

    def __init__(self, topic):

        """
        Parameters
        ----------
        topic : mfit.enumerations.EventTopic
        """

        self._proto = protos.Event()

        self._proto.interfaceVersion = protos.EVENT_INTERFACE_VERSION

        self._proto.topic = topic
        self._proto.correlationId = str(uuid.uuid4())

        # The FromDatetime method expects a naive datetime.
        self._proto.createdAt.FromDatetime(dt=datetime.datetime.utcnow())

    @classmethod
    def from_string(cls, string):
        event = protos.Event.FromString(string)
        return event

    def to_string(self):
        return self._proto.SerializeToString()

    @property
    def arguments(self):
        return self._proto.arguments
