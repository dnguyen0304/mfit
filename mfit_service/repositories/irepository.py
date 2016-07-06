# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class IRepository:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, db_context):
        pass

    @abstractmethod
    def get(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

