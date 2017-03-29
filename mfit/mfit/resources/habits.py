# -*- coding: utf-8 -*-

from . import Base
from mfit import models
from mfit import views

__all__ = ['Habits']


class Habits(Base):

    _model = models.Habits
    _view = views.Habits


Habits._resource = Habits

