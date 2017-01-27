# -*- coding: utf-8 -*-

import collections

import mfit
from . import (_Base,
               AttemptsCollection,
               HabitGroupsCollection,
               HabitsCollection,
               RoutinesCollection,
               UsersCollection)

__all__ = ['Root']


class Root(_Base):

    def get(self):
        data = {
            'subresources': {
                'attempts': mfit.api.url_for(AttemptsCollection, _external=True),
                'habit_groups': mfit.api.url_for(HabitGroupsCollection, _external=True),
                'habits': mfit.api.url_for(HabitsCollection, _external=True),
                'routines': mfit.api.url_for(RoutinesCollection, _external=True),
                'users': mfit.api.url_for(UsersCollection, _external=True)
            }
        }

        urls = {
            'self': mfit.api.url_for(Root, _external=True)
        }

        return collections.OrderedDict([('data', data), ('urls', urls)])

