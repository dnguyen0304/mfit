# -*- coding: utf-8 -*-

import os

import flask
import flask_restful
import nose

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


def main(in_test_mode, test_runner_args):

    """
    References
    ----------
    See the Stack Overflow answer for more details [1].

    .. [1] dbw, "Passing options to nose in a Python test script",
       http://stackoverflow.com/a/13888865

    See Also
    --------
    mfit.app
    """

    if in_test_mode:
        package_directory = os.path.dirname(os.path.abspath(__file__))
        test_runner_args.insert(0, package_directory)
        # While both nose.main() and nose.run() are aliases for
        # nose.TestProgram(), nose.main() exists only for backward
        # compatibility.
        nose.run(argv=test_runner_args)

    elif configuration['environment'] == utilities.Environment.Production.name:
        _app.run()

    else:
        _app.run(debug=True)


__all__ = ['api', 'configuration', 'main']

