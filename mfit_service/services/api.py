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
api.add_resource(resources.UsersWorkouts, '/v1/users/<int:user_id>/workouts/<int:user_workout_id>')
api.add_resource(resources.UsersWorkoutsRelationship, '/v1/users/<int:user_id>/workouts/')
api.add_resource(resources.WorkoutsPrograms, '/v1/workouts/<int:workout_id>/programs/<int:workout_program_id>')
api.add_resource(resources.WorkoutsProgramsRelationship, '/v1/workouts/<int:workout_id>/programs/')

