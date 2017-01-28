# -*- coding: utf-8 -*-

from . import Base
from mfit import models
from mfit import views

__all__ = ['Users']


class Users(Base):

    _model = models.Users
    _view = views.Users


Users._resource = Users

