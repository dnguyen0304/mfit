# -*- coding: utf-8 -*-

from . import Base
from mfit import models
from mfit import views

__all__ = ['HabitGroups']


class HabitGroups(Base):

    _model = models.HabitGroups
    _view = views.HabitGroups


HabitGroups._resource = HabitGroups

