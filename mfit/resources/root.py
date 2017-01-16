# -*- coding: utf-8 -*-

import collections

from mfit import app
from mfit import resources


class Root(resources._Base):

    def get(self):
        data = [
            {
                'users': app.api.url_for(resources.UsersCollection, _external=True)
            },
            {
                'habit_groups': app.api.url_for(resources.HabitGroupsCollection, _external=True)
            },
            {
                'habits': app.api.url_for(resources.HabitsCollection, _external=True)
            },
            {
                'attempts': app.api.url_for(resources.AttemptsCollection, _external=True)
            },
            {
                'routines': app.api.url_for(resources.RoutinesCollection, _external=True)
            }
        ]

        links = {
            'self': app.api.url_for(Root, _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

