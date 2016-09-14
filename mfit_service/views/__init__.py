# -*- coding: utf-8 -*-

from mfit_service.views.base import Base
from mfit_service.views.users import Users
from mfit_service.views.workouts import Workouts
from mfit_service.views.movements import Movements
from mfit_service.views.workouts_movements_units import WorkoutsMovementsUnits
from mfit_service.views.workouts_movements import WorkoutsMovements

__all__ = ['Base',
           'Users',
           'Workouts',
           'WorkoutsMovements',
           'WorkoutsMovementsUnits',
           'Movements']

