# -*- coding: utf-8 -*-

import collections

import mfit
from mfit import resources

__all__ = ['Root']


class Root(resources._Base):

    def get(self):
        data = {
            'subresources': {
                'attempts': mfit.api.url_for(resources.AttemptsCollection, _external=True),
                'habit_groups': mfit.api.url_for(resources.HabitGroupsCollection, _external=True),
                'habits': mfit.api.url_for(resources.HabitsCollection, _external=True),
                'routines': mfit.api.url_for(resources.RoutinesCollection, _external=True),
                'users': mfit.api.url_for(resources.UsersCollection, _external=True)
            }
        }

        urls = {
            'self': mfit.api.url_for(Root, _external=True)
        }

        return collections.OrderedDict([('data', data), ('urls', urls)])

