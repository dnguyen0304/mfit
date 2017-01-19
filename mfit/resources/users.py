# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources
from mfit import views

__all__ = ['Users']


class Users(resources.Base):

    _model = models.Users
    _view = views.Users


Users._resource = Users

