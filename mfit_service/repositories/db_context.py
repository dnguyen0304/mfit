# -*- coding: utf-8 -*-

import sqlalchemy


class DBContext():

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

    """
    def query(self, *args, **kwargs):

    def add(self, entity):
        self._session.add(entity)

    def remove(self, entity):
        self._session.delete(entity)
    """

    def commit(self):

        """
        Returns None

        Commit the local changes to the database.
        """

        self._session.commit()

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

