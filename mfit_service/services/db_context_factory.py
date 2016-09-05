# -*- coding: utf-8 -*-

import sqlalchemy
import sqlalchemy.orm

from mfit_service import services


class DBContextFactory:

    def __init__(self, connection_string):

        """
        Factory class for producing DBContext objects.

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

    def create(self):

        """
        Returns mfit_service.services.DBContext

        Produces an object configured as specified.

        Related Links
        -------------
        1. http://stackoverflow.com/a/12223711
        """

        # Should this dispose the engine, close the connection, and/or
        # close the session?
        session = self._SessionFactory()
        return services.DBContext(session=session)

