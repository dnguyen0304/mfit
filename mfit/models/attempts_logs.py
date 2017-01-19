# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from mfit import models

__all__ = ['AttemptsLogs']


class AttemptsLogs(models.Base):

    __tablename__ = 'attempts_logs'

    id = Column(Integer, primary_key=True)
    attempts_id = Column(ForeignKey('attempts.id'))
    habits_id = Column(ForeignKey('habits.id'))
    sets_remaining = Column()

    attempt = relationship('Attempts', back_populates='logs')
    habit = relationship('Habits', back_populates='attempts_logs')

    def __init__(self, attempt, habit, sets_remaining):

        """
        Attempts Logs model.

        Parameters
        ----------
        attempt : mfit.models.Attempts
            Attempts entity.
        habit : mfit.models.Habits
            Habits entity.
        sets_remaining : int
            Number of remaining sets for the corresponding habit for
            that day.
        """

        self.attempts_id = attempt.id
        self.habits_id = habit.id
        self.sets_remaining = sets_remaining

    def __repr__(self):
        repr_ = '{}(attempt={}, habit={}, sets_remaining={})'
        return repr_.format(self.__class__.__name__,
                            self.attempt,
                            self.habit,
                            self.sets_remaining)

