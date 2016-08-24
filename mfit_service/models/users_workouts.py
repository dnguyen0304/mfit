# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from mfit_service import models


class UsersWorkouts(models.Base):

    __tablename__ = 'users_workouts'

    user_workout_id = Column(primary_key=True)
    user_id = Column(ForeignKey('users.user_id'))
    workout_id = Column(ForeignKey('workouts.workout_id'))
    started_on = Column()
    ends_on = Column()

    # TODO (duyn): Consider using an Association Proxy instead of an
    # Association Object. See this Stack Overflow answer for more
    # details: http://stackoverflow.com/a/7524753.
    user = relationship('Users', back_populates='workouts')
    workout = relationship('Workouts', back_populates='users')
    movements = relationship('UsersWorkoutsMovements', back_populates='user_workout')

    def __init__(self,
                 user,
                 workout,
                 started_on=None,
                 ends_on=None):

        """
        Users workouts model.

        Parameters
        ----------
        user : mfit_service.models.Users
            Users model.
        workout : mfit_service.models.Workouts
            Workouts model.
        started_on : datetime.datetime
            When the user started the workout.
        ends_on : datetime.datetime
            When the workout ends.
        """

        self.user_id = user.user_id
        self.workout_id = workout.workout_id
        self.started_on = started_on
        self.ends_on = ends_on

    def __repr__(self):
        repr_ = '{}(user={}, workout={}, started_on={}, ends_on={})'
        return repr_.format(self.__class__.__name__,
                            self.user,
                            self.workout,
                            self.started_on,
                            self.ends_on)

