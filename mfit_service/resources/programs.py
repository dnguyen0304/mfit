# -*- coding: utf-8 -*-

import flask
import flask_restful
import sqlalchemy
import sqlalchemy.orm

from mfit_service import models
from mfit_service import resources
from mfit_service import services
from mfit_service import views


class Programs(resources.Base):

    def get(self, program_id):
        try:
            program = (
                self._db_context.query(models.WorkoutsMovements)
                                .filter_by(workout_movement_id=program_id)
                                .one())
        except sqlalchemy.orm.exc.NoResultFound:
            return flask_restful.abort(404)
        else:
            return Programs.to_json(program=program)

    def patch(self, program_id):
        program = (
            self._db_context.query(models.WorkoutsMovements)
                            .filter_by(workout_movement_id=program_id)
                            .one())

        for attribute, value in flask.request.get_json().items():
            setattr(program, attribute, value)

        # TODO (duyn): ME-192
        self._db_context.add(program, updated_by=999)
        self._db_context.commit()

        body = Programs.to_json(program=program)

        self._db_context.close()

        return body

    def delete(self, program_id):
        self._db_context.query(models.WorkoutsMovements) \
                        .filter_by(workout_movement_id=program_id) \
                        .delete(synchronize_session=False)
        self._db_context.commit()
        self._db_context.close()

    @staticmethod
    def get_self_link(program):
        self_link = services.api.url_for(
            Programs,
            program_id=program.workout_movement_id,
            _external=True)
        return self_link

    @staticmethod
    def to_json(program):
        links = {
            'self': Programs.get_self_link(program=program)
        }

        body = views.Programs().dump(program).data
        body.update({'links': links})

        return body

