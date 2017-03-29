# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from . import Base

__all__ = ['HabitGroups']


class HabitGroups(Base):

    __tablename__ = 'habit_groups'

    name = Column()

    users = relationship('Attempts', back_populates='habit_group')
    habits = relationship('Routines', back_populates='habit_group')

    def __init__(self, name):

        """
        Habit Groups model.

        Parameters
        ----------
        name : str
            Name.

        Attributes
        ----------
        id : int
            Unique identifier.
        name : str
            Name.
        users : list of mfit.models.Attempts
            Collection of Attempts entities.
        habits : list of mfit.models.Routines
            Collection of Routines entities.
        created_at : datetime.datetime
            When the entity was originally created.
        created_by : int
            Who originally created the entity.
        updated_at : datetime.datetime
            When the entity was last updated.
        updated_by : int
            Who last updated the entity.
        """

        self.name = name

    def __repr__(self):
        repr_ = '{}(name="{}")'
        return repr_.format(self.__class__.__name__, self.name)

