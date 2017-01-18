# -*- coding: utf-8 -*-

import collections
import datetime

import flask
import flask_restful
import sqlalchemy
from sqlalchemy import orm

import mfit


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
        entity : models.Base subclass
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
        SessionFactory = orm.sessionmaker()
        SessionFactory.configure(bind=engine)

        self._SessionFactory = orm.scoped_session(SessionFactory)

    def create(self):

        """
        Produce an object configured as specified.

        Returns
        -------
        resources.base.DBContext

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


class _Base(flask_restful.Resource):

    def __init__(self):
        super().__init__()

        self._db_context_factory = DBContextFactory(
            connection_string=mfit.configuration['repositories']
                                                ['PostgreSQL']
                                                ['connection_string'])
        self._db_context = self._db_context_factory.create()


class Base(_Base):

    _model = None
    _resource = None
    _view = None

    def get(self, id):
        entity = self._get_or_404(id=id)
        return self.to_json(entity=entity)

    def put(self, id):
        entity = self._get_or_404(id=id)

        for attribute, value in flask.request.get_json().items():
            setattr(entity, attribute, value)

        self._db_context.add(entity, updated_by=192)
        self._db_context.commit()
        self._db_context.close()

        return self._resource.to_json(entity=entity)

    def delete(self, id):
        try:
            self._db_context.query(self._model) \
                            .filter_by(id=id) \
                            .delete(synchronize_session=False)
        except (orm.exc.NoResultFound, orm.exc.MultipleResultsFound):
            flask_restful.abort(404)
        self._db_context.commit()
        self._db_context.close()

    def _get_or_404(self, id):

        """
        Parameters
        ----------
        id : int
            Unique identifier.

        Returns
        ------
        models.Base subclass
            Entity.

        Raises
        ------
        werkzeug.exceptions.HTTPException
            If no entities match the given condition or if more than 1
            entity matches the given condition.
        """

        try:
            return self._db_context.query(self._model) \
                                   .filter_by(id=id) \
                                   .one()
        except (orm.exc.NoResultFound, orm.exc.MultipleResultsFound):
            flask_restful.abort(404)

    @classmethod
    def get_self_link(cls, entity):
        return mfit.api.url_for(cls._resource, id=entity.id, _external=True)

    @classmethod
    def to_json(cls, entity):
        data = cls._view().dump(entity).data

        links = {
            'self': cls.get_self_link(entity=entity)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

