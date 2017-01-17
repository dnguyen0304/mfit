# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources
from mfit import views


class Routines(resources.Base):

    _model = models.Routines
    _view = views.Routines


Routines._resource = Routines

