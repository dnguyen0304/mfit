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

        workouts_programs = self._db_context.query(models.WorkoutsMovements) \
                                            .filter_by(workout_id=workout_id) \
                                            .all()

        workouts_programs_uris = [
            resources.WorkoutsPrograms.get_self_link(workout_program=workout_program)
            for workout_program
            in workouts_programs]

        body = collections.OrderedDict([('programs_uris', workouts_programs_uris),
                                        ('links', links)])

        return body

    def post(self):
        workout_program = models.WorkoutsMovements(**flask.request.get_json())

        # TODO (duyn): ME-192
        self._db_context.add(workout_program, created_by=999)
        self._db_context.commit()

        body = resources.WorkoutsPrograms.to_json(workout_program=workout_program)

        self._db_context.close()

        return body

