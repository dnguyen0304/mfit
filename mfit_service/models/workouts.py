# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from mfit_service import models


class Workouts(models.Base):

    __tablename__ = 'workouts'

    workout_id = Column(primary_key=True)
    name = Column()

    # users = relationship('Users',
    #                      secondary='users_workouts',
    #                      back_populates='workouts')
    # movements = relationship('WorkoutsMovements', back_populates='workouts')

    def __init__(self, name):

        """
        Workouts model.

        Parameters
        ----------
        name : String
            Name.
        """

        self.name = name

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

