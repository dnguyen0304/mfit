# -*- coding: utf-8 -*-

import flask
import flask_restful

from mfit import resources
from mfit import utilities

configuration = utilities.get_configuration(project_name=__name__, depth=1)

_app = flask.Flask(__name__)
api = flask_restful.Api(app=_app)

api.add_resource(resources.Root, '/v1/')
api.add_resource(resources.Users, '/v1/users/<int:id>')
api.add_resource(resources.UsersCollection, '/v1/users/')
api.add_resource(resources.HabitGroups, '/v1/habit_groups/<int:id>')
api.add_resource(resources.HabitGroupsCollection, '/v1/habit_groups/')
api.add_resource(resources.Habits, '/v1/habits/<int:id>')
api.add_resource(resources.HabitsCollection, '/v1/habits/')
api.add_resource(resources.Attempts, '/v1/attempts/<int:id>')
api.add_resource(resources.AttemptsCollection, '/v1/attempts/')
api.add_resource(resources.Routines, '/v1/routines/<int:id>')
api.add_resource(resources.RoutinesCollection, '/v1/routines/')
api.add_resource(resources.AttemptsLogs, '/v1/attempts/<int:attempts_id>/logs/<int:id>')
api.add_resource(resources.AttemptsLogsCollection, '/v1/attempts/<int:attempts_id>/logs/')


def main():
    if configuration['environment'] == utilities.Environment.Production.name:
        _app.run()
    else:
        _app.run(debug=True)


__all__ = ['api', 'configuration', 'main']

