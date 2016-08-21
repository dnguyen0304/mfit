# -*- coding: utf-8 -*-

import sqlalchemy

from mfit_service.repositories.db_context import DBContext


class DBContextFactory:

    def __init__(self, connection_string):

        """
        Open a database connection.

        This is a decorator class that extends the SQLAlchemy Session
        Maker object. See the sqlalchemy.orm.session.sessionmaker
        documentation for more details.

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

    def produce(self):

        """
        Related Links
        -------------
        1. http://stackoverflow.com/a/12223711
        """

        # Should this dispose the engine, close the connection, and/or
        # close the session?
        session = self._SessionFactory()
        return DBContext(session=session)

