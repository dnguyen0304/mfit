# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources


class HabitGroupsCollection(resources.BaseCollection):

    _model = models.HabitGroups
    _resource = resources.HabitGroups


HabitGroupsCollection._resource_collection = HabitGroupsCollection

