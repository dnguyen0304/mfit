# -*- coding: utf-8 -*-

from mfit_service.views.base import Base
from mfit_service.views.users import Users
from mfit_service.views.workouts import Workouts
from mfit_service.views.movements import Movements
from mfit_service.views.workouts_programs_units import WorkoutsProgramsUnits
from mfit_service.views.workouts_programs import WorkoutsPrograms

__all__ = ['Base',
           'Users',
           'Workouts',
           'WorkoutsPrograms',
           'WorkoutsProgramsUnits',
           'Movements']

