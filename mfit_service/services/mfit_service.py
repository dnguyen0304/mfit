# -*- coding: utf-8 -*-

from mfit_service import services


class MfitService:
    """
    no public API so you have to use the DBContext directly
    """

    # This should be execute to launch the service and allow API calls.
    def __init__(self, configuration):
        self._db_context_factory = services.DBContextFactory(
            connection_string=configuration['repositories']['PostgreSQL']['connection_string'])
        self._db_context = self._db_context_factory.create()

