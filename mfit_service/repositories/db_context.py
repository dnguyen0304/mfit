# -*- coding: utf-8 -*-

import datetime

import sqlalchemy

from mfit_service.repositories.base_repository import BaseRepository


class DBContext:

    def __init__(self, session):
        # Composition must be used instead of inheritance because the
        # SQLAlchemy Session is always accessed through a factory.
        self._session = session

    def query(self, model):

        """
        Returns None

        This is a decorator method. See the
        sqlalchemy.orm.session.Session documentation for more details.

        Parameters
        ----------
        model : Variable
            Domain model class.
        """

        repositories = {class_.__name__: class_
                        for class_
                        in BaseRepository.__subclasses__()}

        return repositories[model.__name__ + 'Repository'](self._session)

    def add(self, entity, created_by=None, updated_by=None):

        """
        Returns None

        This is a decorator method. See the
        sqlalchemy.orm.session.Session documentation for more details.

        Parameters
        ----------
        entity : Variable
            Domain model instance.
        created_by : datetime.datetime, default None
            Unique identifier for the user who created the entity. This
            parameter is required only when the entity is being
            created.
        updated_by : datetime.datetime, default None
            Unique identifier for the user who updated the entity. This
            parameter is required only when the entity is being
            updated.
        """

        should_be_added = True
        message = 'add() missing 1 required positional argument: "{}"'

        entity_state = sqlalchemy.inspect(entity)

        if entity_state.transient:
            if not created_by:
                raise TypeError(message.format('created_by'))
            else:
                entity.created_on = datetime.datetime.utcnow()
                entity.created_by = created_by
        elif entity_state.persistent:
            if entity not in self._session.dirty:
                should_be_added = False
            elif not updated_by:
                raise TypeError(message.format('updated_by'))
            else:
                entity.updated_on = datetime.datetime.utcnow()
                entity.updated_by = updated_by

        if should_be_added:
            self._session.add(entity)

    def __getattr__(self, name):
        return getattr(self._session, name)

