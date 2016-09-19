# -*- coding: utf-8 -*-

import flask
import flask_restful

from mfit_service import resources

app = flask.Flask(__name__)
api = flask_restful.Api(app=app)

api.add_resource(resources.Root, '/v1/')
api.add_resource(resources.Users, '/v1/users/<int:user_id>')
api.add_resource(resources.UsersCollection, '/v1/users/')
api.add_resource(resources.Workouts, '/v1/workouts/<int:workout_id>')
api.add_resource(resources.WorkoutsCollection, '/v1/workouts/')
api.add_resource(resources.Movements, '/v1/movements/<int:movement_id>')
api.add_resource(resources.MovementsCollection, '/v1/movements/')
api.add_resource(resources.Programs, '/v1/programs/<int:program_id>')
api.add_resource(resources.ProgramsCollection, '/v1/programs/')
api.add_resource(resources.Registrations, '/v1/registrations/<int:registration_id>')
api.add_resource(resources.RegistrationsCollection, '/v1/registrations/')
api.add_resource(resources.UsersWorkoutsLogs, '/v1/users/<int:user_id>/workouts/<int:user_workout_id>/logs/<int:user_workout_log_id>')
api.add_resource(resources.UsersWorkoutsLogsCollection, '/v1/users/<int:user_id>/workouts/<int:user_workout_id>/logs/')

