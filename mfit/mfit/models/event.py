# -*- coding: utf-8 -*-

import datetime
import uuid

from .. import protos


class Event(object):

    def __init__(self, topic, state):

        """
        Parameters
        ----------
        topic : mfit.enumerations.EventTopic
        state : mfit.enumerations.EventState
        """

        self._proto = protos.Event()

        self._proto.interfaceVersion = protos.EVENT_INTERFACE_VERSION

        self._proto.topic = topic
        self._proto.state = state
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
    def topic(self):
        return self._proto.topic

    @property
    def state(self):
        return self._proto.state

    @state.setter
    def state(self, value):
        self._proto.state = value

    @property
    def arguments(self):
        return self._proto.arguments
