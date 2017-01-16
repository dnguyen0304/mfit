# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
from sqlalchemy import orm

import mfit
from mfit import app


class Base(flask_restful.Resource):

    _model = None
    _resource = None
    _view = None

    def __init__(self):
        super().__init__()

        self._db_context_factory = app.DBContextFactory(
            connection_string=mfit.configuration['repositories']
                                                ['PostgreSQL']
                                                ['connection_string'])
        self._db_context = self._db_context_factory.create()

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
        models.Base Subclass
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
        return app.api.url_for(cls._resource, id=entity.id, _external=True)

    @classmethod
    def to_json(cls, entity):
        data = cls._view().dump(entity).data

        links = {
            'self': cls.get_self_link(entity=entity)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

