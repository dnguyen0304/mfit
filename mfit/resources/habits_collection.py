# -*- coding: utf-8 -*-

from . import BaseCollection, Habits
from mfit import models

__all__ = ['HabitsCollection']


class HabitsCollection(BaseCollection):

    _model = models.Habits
    _resource = Habits


HabitsCollection._resource_collection = HabitsCollection

