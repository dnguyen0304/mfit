# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources
from mfit import views


class Attempts(resources.Base):

    _model = models.Attempts
    _view = views.Attempts


Attempts._resource = Attempts

