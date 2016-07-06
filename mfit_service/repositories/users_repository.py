# -*- coding: utf-8 -*-

from mfit_service.models import Users
from mfit_service.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository):

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
        self._model = Users

