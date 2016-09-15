# -*- coding: utf-8 -*-

import collections

import flask

from mfit_service import models
from mfit_service import resources
from mfit_service import services


class WorkoutsProgramsRelationship(resources.Base):

    def get(self, workout_id):
        links = {
            'self': services.api.url_for(WorkoutsProgramsRelationship,
                                         workout_id=workout_id,
                                         _external=True)
        }

        workout_program_uris = []
        body = collections.OrderedDict([('programs', workout_program_uris),
                                        ('links', links)])
        workout_programs = self._db_context.query(models.WorkoutsMovements) \
                                           .filter_by(workout_id=workout_id) \
                                           .all()

        for workout_program in workout_programs:
            self_link = resources.WorkoutsPrograms.get_self_link(
                workout_program=workout_program)
            workout_program_uris.append(self_link)

        return body

    def post(self):
        workout_program = models.WorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(workout_program, created_by=999)
        self._db_context.commit()

        body = resources.WorkoutsPrograms.to_json(workout_program=workout_program)

        self._db_context.close()

        return body

