# -*- coding: utf-8 -*-

from mfit import app
from mfit.resources.base import _Base, Base
from mfit.resources.base_collection import BaseCollection
from mfit.resources.root import Root
from mfit.resources.users import Users
from mfit.resources.users_collection import UsersCollection
from mfit.resources.habit_groups import HabitGroups
from mfit.resources.habit_groups_collection import HabitGroupsCollection
from mfit.resources.habits import Habits
from mfit.resources.habits_collection import HabitsCollection
from mfit.resources.attempts import Attempts
from mfit.resources.attempts_collection import AttemptsCollection
from mfit.resources.routines import Routines
from mfit.resources.routines_collection import RoutinesCollection
from mfit.resources.attempts_logs import AttemptsLogs
from mfit.resources.attempts_logs_collection import AttemptsLogsCollection

__all__ = ['Attempts',
           'AttemptsCollection',
           'AttemptsLogs',
           'AttemptsLogsCollection',
           'Base',
           'BaseCollection',
           'HabitGroups',
           'HabitGroupsCollection',
           'Habits',
           'HabitsCollection',
           'Root',
           'Routines',
           'RoutinesCollection',
           'Users',
           'UsersCollection']

app.api.add_resource(Root, '/v1/')
app.api.add_resource(Users, '/v1/users/<int:id>')
app.api.add_resource(UsersCollection, '/v1/users/')
app.api.add_resource(HabitGroups, '/v1/habit_groups/<int:id>')
app.api.add_resource(HabitGroupsCollection, '/v1/habit_groups/')
app.api.add_resource(Habits, '/v1/habits/<int:id>')
app.api.add_resource(HabitsCollection, '/v1/habits/')
app.api.add_resource(Attempts, '/v1/attempts/<int:id>')
app.api.add_resource(AttemptsCollection, '/v1/attempts/')
app.api.add_resource(Routines, '/v1/routines/<int:id>')
app.api.add_resource(RoutinesCollection, '/v1/routines/')
app.api.add_resource(AttemptsLogs, '/v1/attempts/<int:attempts_id>/logs/<int:id>')
app.api.add_resource(AttemptsLogsCollection, '/v1/attempts/<int:attempts_id>/logs/')

