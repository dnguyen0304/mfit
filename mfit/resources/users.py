# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
from sqlalchemy import orm

from mfit import app
from mfit import models
from mfit import resources
from mfit import views


class Users(resources.Base):

    def get(self, id):
        user = self._get_or_404(id=id)
        return Users.to_json(user=user)

    def put(self, id):
        user = self._get_or_404(id=id)

        for attribute, value in flask.request.get_json().items():
            setattr(user, attribute, value)

        self._db_context.add(user, updated_by=192)
        self._db_context.commit()

        body = Users.to_json(user=user)

        self._db_context.close()

        return body

    def delete(self, id):
        try:
            self._db_context.query(models.Users) \
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
        models.Users
            Users entity.

        Raises
        ------
        werkzeug.exceptions.HTTPException
            If no entities match the given condition or if more than 1
            entity matches the given condition.
        """

        try:
            return self._db_context.query(models.Users) \
                       .filter_by(id=id) \
                       .one()
        except (orm.exc.NoResultFound, orm.exc.MultipleResultsFound):
            flask_restful.abort(404)

    @staticmethod
    def get_self_link(user):
        return app.api.url_for(Users, id=user.id, _external=True)

    @staticmethod
    def to_json(user):
        body = collections.OrderedDict()

        data = views.Users().dump(user).data

        links = {
            'self': Users.get_self_link(user=user)
        }

        body.update({'data': data})
        body.update({'links': links})

        return body

