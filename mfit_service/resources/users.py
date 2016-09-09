# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class Users(resources.Base):

    def get(self, user_id):
        try:
            user = self._db_context.query(models.Users) \
                                   .filter_by(user_id=user_id) \
                                   .one()
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return Users.to_json(user=user)

    def patch(self, user_id):
        user = self._db_context.query(models.Users) \
                               .filter_by(user_id=user_id) \
                               .one()

        for attribute, value in flask.request.get_json().items():
            setattr(user, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(user, updated_by=999)
        self._db_context.commit()

        body = Users.to_json(user=user)

        self._db_context.close()

        return body

    def delete(self, user_id):
        self._db_context.query(models.Users) \
                        .filter_by(user_id=user_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(user):
        self_link = services.api.url_for(Users,
                                         user_id=user.user_id,
                                         _external=True)
        return self_link

    @staticmethod
    def to_json(user):
        links = {
            'self': Users.get_self_link(user=user)
        }

        data = {
            'type': 'users',
            'id': str(user.user_id),
            'attributes': user.to_json()
        }

        body = collections.OrderedDict([('links', links), ('data', data)])

        return body

