# -*- coding: utf-8 -*-

from . import Base
from mfit import models
from mfit import views

__all__ = ['Routines']


class Routines(Base):

    _model = models.Routines
    _view = views.Routines


Routines._resource = Routines

