# -*- coding: utf-8 -*-

from mfit_service.views.base import Base
from mfit_service.views.users import Users
from mfit_service.views.workouts import Workouts
from mfit_service.views.movements import Movements
from mfit_service.views.programs_units import ProgramsUnits
from mfit_service.views.programs import Programs
from mfit_service.views.registrations import Registrations
from mfit_service.views.registrations_logs import RegistrationsLogs

__all__ = ['Base',
           'Movements',
           'Programs',
           'ProgramsUnits',
           'Registrations',
           'RegistrationsLogs',
           'Users',
           'Workouts']

