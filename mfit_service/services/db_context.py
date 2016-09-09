# -*- coding: utf-8 -*-

import datetime

import sqlalchemy


class DBContext:

    def __init__(self, session):

        """
        Manages persistence operations for ORM-mapped objects.

        This is a decorator class that extends the SQLAlchemy Session
        Maker object. See the sqlalchemy.orm.session.Session
        documentation for more details.

        Parameters
        ----------
        session : sqlalchemy.orm.session.Session
            Session instance.
        """

        # Composition must be used instead of inheritance because the
        # SQLAlchemy Session is always accessed through a factory.
        self._session = session

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
            if created_by is None:
                raise TypeError(message.format('created_by'))
            else:
                entity.created_on = datetime.datetime.utcnow()
                entity.created_by = created_by
        elif entity_state.persistent:
            if entity not in self._session.dirty:
                should_be_added = False
            elif updated_by is None:
                raise TypeError(message.format('updated_by'))
            else:
                entity.updated_on = datetime.datetime.utcnow()
                entity.updated_by = updated_by

        if should_be_added:
            self._session.add(entity)

    def __getattr__(self, name):
        return getattr(self._session, name)

