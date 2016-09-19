# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class ProgramsCollection(resources.Base):

    def get(self):
        links = {
            'self': services.api.url_for(ProgramsCollection, _external=True)
        }

        programs_uris = [
            resources.Programs.get_self_link(program=program)
            for program
            in self._db_context.query(models.WorkoutsMovements).all()]

        body = collections.OrderedDict([('programs_uris', programs_uris),
                                        ('links', links)])

        return body

    def post(self):
        program = models.WorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(program, created_by=999)
        self._db_context.commit()

        body = resources.Programs.to_json(program=program)

        self._db_context.close()

        return body

