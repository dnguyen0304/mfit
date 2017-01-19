# -*- coding: utf-8 -*-

from mfit.views.base import Base
from mfit.views.habit_groups import HabitGroups
from mfit.views.habits import Habits
from mfit.views.users import Users
from mfit.views.attempts import Attempts
from mfit.views.routines import Routines
from mfit.views.attempts_logs import AttemptsLogs

__all__ = ['Attempts',
           'AttemptsLogs',
           'Base',
           'HabitGroups',
           'Habits',
           'Routines',
           'Users']

