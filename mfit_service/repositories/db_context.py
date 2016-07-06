# -*- coding: utf-8 -*-

import datetime

import sqlalchemy


class DBContext:

    def __init__(self, connection_string, **kwargs):

        """
        Open a database connection.

        Parameters
        ----------
        connection_string : String
            Formatted string containing host and authentication
            information.
        """

        url = 'postgresql+psycopg2://' + connection_string

        engine = sqlalchemy.create_engine(url)
        SessionFactory = sqlalchemy.orm.sessionmaker()
        SessionFactory.configure(bind=engine)

        self._SessionFactory = sqlalchemy.orm.scoped_session(SessionFactory)
        self._session = self._SessionFactory()

    def add(self, entity):

        """
        See the mfit_service.repositories.BaseRepository source
        documentation for more details.
        """

        self._session.add(entity)

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

    def remove(self, entity):

        """
        See the mfit_service.repositories.BaseRepository source
        documentation for more details.
        """

        self._session.delete(entity)

    def query(self, model, *args, **kwargs):

        """
        See the mfit_service.repositories.BaseRepository source
        documentation for more details.

        Parameters
        ----------
        model : Variable
            Domain model class.
        """

        return self._session.query(model)

    def commit(self):

        """
        Returns None

        Commit the local changes to the database.
        """

        self._session.commit()

    def rollback(self):

        """
        Returns None

        Rollback the transaction.
        """

        self._session.rollback()

    def dispose(self):

        """
        Returns None

        Close the database connection.
        """

        self._session.close()

    def refresh(self):

        """
        Returns None

        Reset the state of the database context.

        This method is intended to provide a convenient way of managing
        database context scope.

        Related Links
        -------------
        1. http://stackoverflow.com/a/12223711
        """

        # Should this dispose the engine, close the connection, and/or
        # close the session?
        self.dispose()
        self._session = self._SessionFactory()

