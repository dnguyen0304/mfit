# -*- coding: utf-8 -*-

from sqlalchemy import Column

from mfit_service import models


class WorkoutsMovementsUnits(models.Base):

    __tablename__ = 'workouts_movements_units'

    workout_movement_unit_id = Column(primary_key=True)
    name = Column()

    def __init__(self, name):

        """
        Workouts movements units model.

        Parameters
        ----------
        name : String
            Name.
        """

        self.name = name

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

