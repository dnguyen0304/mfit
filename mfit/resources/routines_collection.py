# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources

__all__ = ['RoutinesCollection']


class RoutinesCollection(resources.BaseCollection):

    _model = models.Routines
    _resource = resources.Routines


RoutinesCollection._resource_collection = RoutinesCollection
