# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources


class AttemptsCollection(resources.BaseCollection):

    _model = models.Attempts
    _resource = resources.Attempts


AttemptsCollection._resource_collection = AttemptsCollection

