# -*- coding: utf-8 -*-

from mfit_service.resources.base import Base
from mfit_service.resources.root import Root
from mfit_service.resources.users import Users
from mfit_service.resources.users_collection import UsersCollection
from mfit_service.resources.workouts import Workouts
from mfit_service.resources.workouts_collection import WorkoutsCollection
from mfit_service.resources.movements import Movements
from mfit_service.resources.movements_collection import MovementsCollection
from mfit_service.resources.programs import Programs
from mfit_service.resources.programs_collection import ProgramsCollection
from mfit_service.resources.users_workouts import UsersWorkouts
from mfit_service.resources.users_workouts_relationship import UsersWorkoutsRelationship
from mfit_service.resources.users_workouts_logs import UsersWorkoutsLogs
from mfit_service.resources.users_workouts_logs_collection import UsersWorkoutsLogsCollection

__all__ = ['Base',
           'Movements',
           'MovementsCollection',
           'Programs',
           'ProgramsCollection',
           'Root',
           'Users',
           'UsersCollection',
           'UsersWorkouts',
           'UsersWorkoutsLogs',
           'UsersWorkoutsLogsCollection',
           'UsersWorkoutsRelationship',
           'Workouts',
           'WorkoutsCollection']

