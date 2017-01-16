# -*- coding: utf-8 -*-

import collections

import flask
import flask_restful
from sqlalchemy import orm

from mfit import app
from mfit import models
from mfit import resources
from mfit import views


class HabitGroups(resources.Base):

    def get(self, id):
        habit_group = self._get_or_404(id=id)
        return HabitGroups.to_json(habit_group=habit_group)

    def patch(self, id):
        habit_group = self._get_or_404(id=id)

        for attribute, value in flask.request.get_json().items():
            setattr(habit_group, attribute, value)

        self._db_context.add(habit_group, updated_by=192)
        self._db_context.commit()
        self._db_context.close()

        return HabitGroups.to_json(habit_group=habit_group)

    def delete(self, id):
        try:
            self._db_context.query(models.HabitGroups) \
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
        models.HabitGroups
            Habit Groups entity.

        Raises
        ------
        werkzeug.exceptions.HTTPException
            If no entities match the given condition or if more than 1
            entity matches the given condition.
        """

        try:
            return self._db_context.query(models.HabitGroups) \
                                   .filter_by(id=id) \
                                   .one()
        except (orm.exc.NoResultFound, orm.exc.MultipleResultsFound):
            flask_restful.abort(404)

    @staticmethod
    def get_self_link(habit_group):
        return app.api.url_for(HabitGroups, id=habit_group.id, _external=True)

    @staticmethod
    def to_json(habit_group):
        body = collections.OrderedDict()

        data = views.HabitGroups().dump(habit_group).data

        links = {
            'self': HabitGroups.get_self_link(habit_group=habit_group)
        }

        body.update({'data': data})
        body.update({'links': links})

        return body

