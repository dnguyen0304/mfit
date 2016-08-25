# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from mfit_service import models


class UsersWorkoutsMovements(models.Base):

    __tablename__ = 'users_workouts_movements'

    user_workout_movement_id = Column(primary_key=True)
    user_workout_id = Column(ForeignKey('users_workouts.user_workout_id'))
    movement_id = Column(ForeignKey('movements.movement_id'))
    sets_remaining = Column()

    user_workout = relationship('UsersWorkouts', back_populates='movements')
    movement = relationship('Movements', back_populates='users_workouts')

    def __init__(self,
                 user_workout,
                 movement,
                 sets_remaining):

        """
        Users workouts movements model.

        Parameters
        ----------
        user_workout : mfit_service.models.UsersWorkouts
            Users workouts model.
        movement : mfit_service.models.Movements
            Movements model.
        sets_remaining : Integer
            Number of remaining sets for the movement for that day.
        """

        self.user_workout_id = user_workout.user_workout_id
        self.movement_id = movement.movement_id
        self.sets_remaining = sets_remaining

    def __repr__(self):
        repr_ = '{}(user_workout={}, movement={}, sets_remaining={})'
        return repr_.format(self.__class__.__name__,
                            self.user_workout,
                            self.movement,
                            self.sets_remaining)

