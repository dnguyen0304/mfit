# -*- coding: utf-8 -*-

from mfit_service.resources.base import Base
from mfit_service.resources.root import Root
from mfit_service.resources.users import Users
from mfit_service.resources.users_collection import UsersCollection
from mfit_service.resources.workouts import Workouts
from mfit_service.resources.workouts_collection import WorkoutsCollection
from mfit_service.resources.movements import Movements
from mfit_service.resources.movements_collection import MovementsCollection
from mfit_service.resources.workouts_movements import WorkoutsMovements
from mfit_service.resources.workouts_movements_relationships import WorkoutsMovementsRelationships

__all__ = ['Base',
           'Root',
           'Users',
           'UsersCollection',
           'Workouts',
           'WorkoutsCollection',
           'WorkoutsMovements',
           'WorkoutsMovementsRelationships',
           'Movements',
           'MovementsCollection']

