# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

__all__ = ['Routines']


class Routines(Base):

    __tablename__ = 'routines'

    habit_groups_id = Column(ForeignKey('habit_groups.id'))
    habits_id = Column(ForeignKey('habits.id'))
    # TODO (duyn): Should this field name be singular?
    sets = Column()
    value = Column()
    routines_units_id = Column(ForeignKey('routines_units.id'))
    sort_order = Column()

    habit_group = relationship('HabitGroups', back_populates='habits')
    habit = relationship('Habits', back_populates='habit_groups')
    routines_unit = relationship('RoutinesUnits')

    def __init__(self,
                 habit_group,
                 habit,
                 sets,
                 value,
                 routines_unit,
                 sort_order=1):

        """
        Routines model.

        Parameters
        ----------
        habit_group : mfit.models.HabitGroups
            Habit Groups entity.
        habit : mfit.models.Habits
            Habits entity.
        sets : int
            Number of sets for the corresponding habit.
        value : int
            Number of units (repetitions, seconds, etc.) per set.
        routines_unit : mfit.models.RoutinesUnits
            Routines Units entity.
        sort_order : int, optional
            Sort order. Defaults to 1.

        Attributes
        ----------
        id : int
            Unique identifier.
        habit_group : mfit.models.HabitGroups
            Habit Groups entity.
        habit_groups_id : int
            Habit Groups unique identifier.
        habit : mfit.models.Habits
            Habits entity.
        habit_id : int
            Habits unique identifier.
        sets : int
            Number of sets for the corresponding habit.
        value : int
            Number of units (repetitions, seconds, etc.) per set.
        routines_unit : mfit.models.RoutinesUnits
            Routines Units entity.
        routines_units_id : int
            Routines Units unique identifier.
        sort_order : int, optional
            Sort order. Defaults to 1.
        created_at : datetime.datetime
            When the entity was originally created.
        created_by : int
            Who originally created the entity.
        updated_at : datetime.datetime
            When the entity was last updated.
        updated_by : int
            Who last updated the entity.
        """

        self.habit_groups_id = habit_group.id
        self.habits_id = habit.id
        self.sets = sets
        self.value = value
        self.routines_units_id = routines_unit.id
        # TODO (duyn): Should this value be set by the DBContext?
        self.sort_order = sort_order

    def __repr__(self):
        repr_ = '{}(habit_group={}, habit={}, sets={}, value={}, routines_unit={}, sort_order={})'
        return repr_.format(self.__class__.__name__,
                            self.habit_group,
                            self.habit,
                            self.sets,
                            self.value,
                            self.routines_unit,
                            self.sort_order)

