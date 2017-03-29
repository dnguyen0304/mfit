# -*- coding: utf-8 -*-

from . import BaseCollection, HabitGroups
from mfit import models

__all__ = ['HabitGroupsCollection']


class HabitGroupsCollection(BaseCollection):

    _model = models.HabitGroups
    _resource = HabitGroups


HabitGroupsCollection._resource_collection = HabitGroupsCollection

