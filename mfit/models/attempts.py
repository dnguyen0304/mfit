# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from mfit import models


class Attempts(models.Base):

    __tablename__ = 'attempts'

    id = Column(Integer, primary_key=True)
    users_id = Column(ForeignKey('users.id'))
    habit_groups_id = Column(ForeignKey('habit_groups.id'))
    # Should these attributes use past tense verbs for consistency?
    starts_at = Column()
    ends_at = Column()

    # References
    # ----------
    # See the Stack Overflow answer for more details [1].
    #
    # .. [1] SingleNegationElimination, "SQLAlchemy ManyToMany
    #   secondary table with additional fields,"
    #   http://stackoverflow.com/a/7524753.
    user = relationship('Users', back_populates='habit_groups')
    habit_group = relationship('HabitGroups', back_populates='users')
    logs = relationship('AttemptsLogs', back_populates='attempt')

    def __init__(self, user, habit_group, starts_at=None, ends_at=None):

        """
        Attempts model.

        Parameters
        ----------
        user : mfit.models.Users
            Users entity.
        habit_group : mfit.models.HabitGroups
            Habit Groups entity.
        starts_at : datetime.datetime, optional
            When the workout starts. Defaults to `None`.
        ends_at : datetime.datetime, optional
            When the workout ends. Defaults to `None`.

        Attributes
        ----------
        id : int
            Unique identifier.
        users_id : int
            Users unique identifier.
        habit_groups_id : int
            Habit Groups unique identifier.
        user : mfit.models.Users
            Users entity.
        habit_group : mfit.models.HabitGroups
            Habit Groups entity.
        starts_at : datetime.datetime, optional
            When the attempt starts. Defaults to `None`.
        ends_at : datetime.datetime, optional
            When the attempt ends. Defaults to `None`.
        logs : list of mfit.models.AttemptsLogs
            Collection of Attempts Logs entities.
        created_at : datetime.datetime
            When the entity was originally created.
        created_by : int
            Who originally created the entity.
        updated_at : datetime.datetime
            When the entity was last updated.
        updated_by : int
            Who last updated the entity.
        """

        self.users_id = user.id
        self.habit_groups_id = habit_group.id
        self.starts_at = starts_at
        self.ends_at = ends_at

    def __repr__(self):
        repr_ = '{}(user={}, habit_group={}, starts_at={}, ends_at={})'
        return repr_.format(self.__class__.__name__,
                            self.user,
                            self.habit_group,
                            self.starts_at,
                            self.ends_at)

