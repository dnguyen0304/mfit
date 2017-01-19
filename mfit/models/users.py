# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from mfit import models

__all__ = ['Users']


class Users(models.Base):

    __tablename__ = 'users'

    email_address = Column()
    first_name = Column()
    last_name = Column()

    habit_groups = relationship('Attempts', back_populates='user')

    def __init__(self, email_address, first_name, last_name):

        """
        Users model.

        Parameters
        ----------
        email_address : str
            Email address.
        first_name : str
            Forename.
        last_name : str
            Surname.

        Attributes
        ----------
        id : int
            Unique identifier.
        email_address : str
            Email address.
        first_name : str
            Forename.
        last_name : str
            Surname.
        habit_groups : list of mfit.models.Attempts
            Collection of Attempts entities.
        created_at : datetime.datetime
            When the entity was originally created.
        created_by : int
            Who originally created the entity.
        updated_at : datetime.datetime
            When the entity was last updated.
        updated_by : int
            Who last updated the entity.
        """

        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        repr_ = '{}(email_address="{}", first_name="{}", last_name="{}")'
        return repr_.format(self.__class__.__name__,
                            self.email_address,
                            self.first_name,
                            self.last_name)

