# -*- coding: utf-8 -*-

from . import Base
from mfit import models
from mfit import views


class Attempts(Base):

    _model = models.Attempts
    _view = views.Attempts


Attempts._resource = Attempts

