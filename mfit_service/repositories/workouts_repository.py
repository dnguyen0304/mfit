# -*- coding: utf-8 -*-

from mfit_service.models import Workouts
from mfit_service.repositories import BaseRepository


class WorkoutsRepository(BaseRepository):

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
        self._model = Workouts

