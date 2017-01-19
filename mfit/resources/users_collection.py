# -*- coding: utf-8 -*-

from mfit import models
from mfit import resources

__all__ = ['UsersCollection']


class UsersCollection(resources.BaseCollection):

    _model = models.Users
    _resource = resources.Users


UsersCollection._resource_collection = UsersCollection

