# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey

from mfit_service import models


class UsersWorkouts(models.Base):

    __tablename__ = 'users_workouts'

    user_workout_id = Column(primary_key=True)
    user_id = Column(ForeignKey('users.user_id'))
    workout_id = Column(ForeignKey('workouts.workout_id'))

    def __init__(self, user_id, workout_id):

        """
        Users workouts model.

        Parameters
        ----------
        user_id : Integer
            User unique identifier
        workout_id : Integer
            Workout unique identifier
        """

        self.user_id = user_id
        self.workout_id = workout_id

    def __repr__(self):
        repr_ = '{}(user_id={}, workout_id={})'
        return repr_.format(self.__class__.__name__,
                            self.user_id,
                            self.workout_id)

