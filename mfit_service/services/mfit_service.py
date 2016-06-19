# -*- coding: utf-8 -*-

import json
import os

from mfit_service import repositories


class MfitService():

    def __init__(self):
        project_directory = os.path.dirname(os.path.realpath(__file__)) + '/../../'

        try:
            environment = os.environ['MFITSERVICE_ENVIRONMENT']
        except KeyError:
            message = 'An environment variable is missing. '
            suggestion = ("""Try checking the environment variables. """
                          """MFITSERVICE_ENVIRONMENT should be set """
                          """to Production", "Development", etc.""")
            raise EnvironmentError(message + suggestion)

        with open(project_directory + 'project.config', 'r') as file:
            self._configuration = json.loads(file.read())[environment]

        self._db_context = repositories.DBContext(
            connection_string=self._configuration['repositories']['PostgreSQL']['connection_string'])

    def bind_repository_many(self, blah):

        """
        Returns None

        Bind repositories to the service dynamically.

        Parameters
        ----------
        repositories : Iterable
            Collection of objects implementing the
            mfit_service.repositories.IRepository interface.
        """

        for repository in blah:
            repository_ = repository(db_context=self._db_context)
            setattr(self, repository_.__class__.__name__, repository_)

    def commit(self):

        """
        See the mfit_service.repositories.DBContext source
        documentation for more details.
        """

        self._db_context.commit()

    def rollback(self):

        """
        See the mfit_service.repositories.DBContext source
        documentation for more details.
        """

        self._db_context.rollback()

    def dispose(self):

        """
        See the mfit_service.repositories.DBContext source
        documentation for more details.
        """

        self._db_context.dispose()

    def refresh(self):

        """
        See the mfit_service.repositories.DBContext source
        documentation for more details.
        """

        self._db_context.refresh()

