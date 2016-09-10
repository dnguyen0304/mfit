# -*- coding: utf-8 -*-

import collections

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from mfit_service import models


class Movements(models.Base):

    __tablename__ = 'movements'

    movement_id = Column(primary_key=True)
    name = Column()

    workouts = relationship('WorkoutsMovements', back_populates='movement')
    users_workouts = relationship('UsersWorkoutsMovements', back_populates='movement')

    def __init__(self, name):

        """
        Movements model.

        Parameters
        ----------
        name : String
            Name.
        """

        self.name = name

    def _to_json_helper(self):
        return collections.OrderedDict([('id', str(self.movement_id)),
                                        ('name', self.name)])

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

