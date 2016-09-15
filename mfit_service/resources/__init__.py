# -*- coding: utf-8 -*-

from mfit_service.resources.base import Base
from mfit_service.resources.root import Root
from mfit_service.resources.users import Users
from mfit_service.resources.users_collection import UsersCollection
from mfit_service.resources.workouts import Workouts
from mfit_service.resources.workouts_collection import WorkoutsCollection
from mfit_service.resources.movements import Movements
from mfit_service.resources.movements_collection import MovementsCollection
from mfit_service.resources.workouts_programs import WorkoutsPrograms
from mfit_service.resources.workouts_programs_relationship import WorkoutsProgramsRelationship

__all__ = ['Base',
           'Root',
           'Users',
           'UsersCollection',
           'Workouts',
           'WorkoutsCollection',
           'WorkoutsPrograms',
           'WorkoutsProgramsRelationship',
           'Movements',
           'MovementsCollection']

