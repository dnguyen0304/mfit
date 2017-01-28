# -*- coding: utf-8 -*-

from . import Attempts, BaseCollection
from mfit import models


class AttemptsCollection(BaseCollection):

    _model = models.Attempts
    _resource = Attempts


AttemptsCollection._resource_collection = AttemptsCollection

