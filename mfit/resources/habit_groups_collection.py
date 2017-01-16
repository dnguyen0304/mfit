# -*- coding: utf-8 -*-

import collections

import flask

from mfit import app
from mfit import models
from mfit import resources


class HabitGroupsCollection(resources.BaseCollection):

    def get(self):
        data = [resources.HabitGroups.get_self_link(entity=habit_group)
                for habit_group
                in self._db_context.query(models.HabitGroups).all()]

        links = {
            'self': app.api.url_for(HabitGroupsCollection, _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

    def post(self):
        habit_group = models.HabitGroups(**flask.request.get_json())

        self._db_context.add(habit_group, created_by=192)
        self._db_context.commit()
        self._db_context.close()

        return resources.HabitGroups.to_json(entity=habit_group)

