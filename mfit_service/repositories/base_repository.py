# -*- coding: utf-8 -*-

import datetime

import sqlalchemy

from mfit_service.repositories.irepository import IRepository


class BaseRepository(IRepository):

    def get(self, entity_id):

        """
        Returns Variable

        Get the existing entity from the database.

        Parameters
        ----------
        entity_id : Integer
            Entity unique identifier.
        """

        primary_key = sqlalchemy.inspect(self._model).primary_key[0]
        entity = self._db_context.query(self._model) \
                                 .filter_by(**{primary_key.name: entity_it}) \
                                 .one()
        return entity

    def get_all(self):

        """
        Returns List

        Get all existing entities from the database.
        """

        entities = self._db_context.query(self._model).all()
        return entities

    def add(self, entity, created_by=-1):

        """
        Returns None

        Add the new entity to the database.

        Parameters
        ----------
        entity : Variable
            Domain model instance.
        """

        entity.created_on = datetime.datetime.utcnow()
        entity.created_by = created_by

        self._db_context.add(entity)

    def remove(self, entity):

        """
        Returns None

        Remove the existing entity from the database.

        Parameters
        ----------
        entity : Variable
            Domain model instance.
        """

        self._db_context.remove(entity)

