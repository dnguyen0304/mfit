# -*- coding: utf-8 -*-

import datetime

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit import resources

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

api.add_resource(resources.Root, '/v1/')
api.add_resource(resources.Users, '/v1/users/<int:id>')
api.add_resource(resources.UsersCollection, '/v1/users/')


class DBContext:

    def __init__(self, session):

        """
        Decorator class that manages persistence operations for
        ORM-mapped objects.

        Parameters
        ----------
        session : sqlalchemy.orm.session.Session
            Session instance.

        See Also
        --------
        sqlalchemy.orm.session.Session
        """

        # Composition must be used instead of inheritance because
        # SQLAlchemy Sessions are always accessed through a factory.
        self._session = session

    def add(self, entity, created_by=None, updated_by=None):

        """
        Decorator method.

        Extends the SQLAlchemy Session's `add()` to require specifying
        the `created_by` or `updated_by` information given the
        respective condition. The appropriate `created_at` or
        `updated_at` field is set to the current UTC date and time.

        Parameters
        ----------
        entity : Variable
            Domain model instance.
        created_by : datetime.datetime, optional
            Unique identifier for the user who created the entity. This
            parameter is required only when the entity is being
            created. Defaults to `None`.
        updated_by : datetime.datetime, optional
            Unique identifier for the user who updated the entity. This
            parameter is required only when the entity is being
            updated. Defaults to `None`.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            If the `created_by` or `updated_by` information was not
            specified given the respective condition.

        See Also
        --------
        sqlalchemy.orm.session.Session
        """

        should_be_persisted = True
        message = 'add() missing 1 required positional argument: "{}"'

        entity_state = sqlalchemy.inspect(entity)

        if entity_state.transient:
            if created_by is None:
                raise TypeError(message.format('created_by'))
            else:
                entity.created_at = datetime.datetime.utcnow()
                entity.created_by = created_by
        elif entity_state.persistent:
            if entity not in self._session.dirty:
                should_be_persisted = False
            elif updated_by is None:
                raise TypeError(message.format('updated_by'))
            else:
                entity.updated_at = datetime.datetime.utcnow()
                entity.updated_by = updated_by

        if should_be_persisted:
            self._session.add(entity)

    def __getattr__(self, name):
        return getattr(self._session, name)


class DBContextFactory:

    def __init__(self, connection_string):

        """
        Factory class for producing DBContexts.

        Parameters
        ----------
        connection_string : str
            Formatted string containing host and authentication
            information.
        """

        engine = sqlalchemy.create_engine(connection_string)
        SessionFactory = sqlalchemy.orm.sessionmaker()
        SessionFactory.configure(bind=engine)

        self._SessionFactory = sqlalchemy.orm.scoped_session(SessionFactory)

    def create(self):

        """
        Produce an object configured as specified.

        Returns
        -------
        DBContext

        References
        ----------
        See the Stack Overflow answer for more details [1].

        .. [1] zzzeek, "SQLAlchemy: Creating vs. Reusing a Session",
           http://stackoverflow.com/a/12223711.
        """

        # Should this dispose the engine, close the connection, and / or
        # close the session?
        session = self._SessionFactory()
        return DBContext(session=session)

