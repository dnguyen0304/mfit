# -*- coding: utf-8 -*-

from . import BaseCollection, Users
from mfit import models

__all__ = ['UsersCollection']


class UsersCollection(BaseCollection):

    _model = models.Users
    _resource = Users


UsersCollection._resource_collection = UsersCollection

