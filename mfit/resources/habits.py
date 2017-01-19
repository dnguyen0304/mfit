# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources
from mfit import views

__all__ = ['Habits']


class Habits(resources.Base):

    _model = models.Habits
    _view = views.Habits


Habits._resource = Habits

