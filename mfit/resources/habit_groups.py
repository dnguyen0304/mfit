# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources
from mfit import views

__all__ = ['HabitGroups']


class HabitGroups(resources.Base):

    _model = models.HabitGroups
    _view = views.HabitGroups


HabitGroups._resource = HabitGroups
