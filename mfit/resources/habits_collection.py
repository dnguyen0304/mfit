# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources

__all__ = ['HabitsCollection']


class HabitsCollection(resources.BaseCollection):

    _model = models.Habits
    _resource = resources.Habits


HabitsCollection._resource_collection = HabitsCollection

