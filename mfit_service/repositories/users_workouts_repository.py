# -*- coding: utf-8 -*-

from mfit_service.models import UsersWorkouts
from mfit_service.repositories.base_repository import BaseRepository


class UsersWorkoutsRepository(BaseRepository):

    def __init__(self, db_context):

        """
        Mediates between the domain and data mapping layers, acting
        like an in-memory collection of domain objects.

        Parameters
        ----------
        db_context : mfit_service.repositories.DBContext
            DBContext.
        """

        self._db_context = db_context
        self._model = UsersWorkouts
