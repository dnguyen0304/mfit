# -*- coding: utf-8 -*-

import collections

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from mfit_service import models


class Workouts(models.Base):

    __tablename__ = 'workouts'

    workout_id = Column(primary_key=True)
    name = Column()

    users = relationship('UsersWorkouts', back_populates='workout')
    movements = relationship('WorkoutsMovements', back_populates='workout')

    def __init__(self, name):

        """
        Workouts model.

        Parameters
        ----------
        name : String
            Name.
        """

        self.name = name

    def to_json(self):

        """
        Return Dictionary

        Convert the object into a JSON representation.
        """

        return collections.OrderedDict([('name', self.name)])

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

