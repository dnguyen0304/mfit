# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from mfit_service import models


class WorkoutsMovements(models.Base):

    __tablename__ = 'workouts_movements'

    workout_movement_id = Column(primary_key=True)
    workout_id = Column(ForeignKey('workouts.workout_id'))
    movement_id = Column(ForeignKey('movements.movement_id'))
    sets = Column()
    value = Column()
    workout_movement_unit_id = Column(
        ForeignKey('workouts_movements_units.workout_movement_unit_id'))
    sort_order = Column()

    workout = relationship('Workouts', back_populates='movements')
    movement = relationship('Movements', back_populates='workouts')
    workout_movement_unit = relationship('WorkoutsMovementsUnits')

    def __init__(self,
                 workout,
                 movement,
                 sets,
                 value,
                 workout_movement_unit,
                 sort_order=1):

        """
        Workouts movements model.

        Parameters
        ----------
        workout : mfit_service.models.Workouts
            Workouts model.
        movement : mfit_service.models.Movements
            Movements model.
        sets : Integer
            Number of movement sets per workout.
        value : Integer
            Number of movement units (repetitions, seconds, etc.) per
            movement set.
        workout_movement_unit : mfit_service.models.WorkoutsMovementsUnits
            Workout movements unit model.
        sort_order : Integer, default 1
            Sort order.
        """

        self.workout_id = workout.workout_id
        self.movement_id = movement.movement_id
        self.sets = sets
        self.value = value
        self.workout_movement_unit_id = workout_movement_unit.workout_movement_unit_id
        #TODO(duyn): should set this in the repository
        self.sort_order = sort_order

    def __repr__(self):
        repr_ = '{}(workout={}, movement={}, sets={}, value={}, workout_movement_unit={}, sort_order={})'
        return repr_.format(self.__class__.__name__,
                            self.workout,
                            self.movement,
                            self.sets,
                            self.value,
                            self.workout_movement_unit,
                            self.sort_order)

