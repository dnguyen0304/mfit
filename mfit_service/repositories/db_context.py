# -*- coding: utf-8 -*-

import datetime

import sqlalchemy


class DBContext:

    def __init__(self, connection_string):

        """
        Open a database connection.

        This is a decorator class that extends the SQLAlchemy Session
        object. See the sqlalchemy.orm.session.Session documentation
        for more details.

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

    def add(self, entity, created_by=None, updated_by=None):

        """
        Returns None

        Add the new entity to the database.

        This is a decorator method. See the
        sqlalchemy.orm.session.Session documentation for more details.

        Parameters
        ----------
        entity : Variable
            Domain model instance.
        created_by : datetime.datetime
        updated_by : datetime.datetime
        """

        entity.created_on = datetime.datetime.utcnow()
        entity.created_by = created_by
        entity.updated_by = updated_by

        self._session.add(entity)

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
        self._session.close()
        self._session = self._SessionFactory()

    def __getattr__(self, name):
        return getattr(self._session, name)

