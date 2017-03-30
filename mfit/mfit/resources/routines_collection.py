# -*- coding: utf-8 -*-

from . import BaseCollection, Routines
from mfit import models

__all__ = ['RoutinesCollection']


class RoutinesCollection(BaseCollection):

    _model = models.Routines
    _resource = Routines


RoutinesCollection._resource_collection = RoutinesCollection

