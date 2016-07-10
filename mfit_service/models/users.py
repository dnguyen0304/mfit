# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.orm import relationship

from mfit_service import models


class Users(models.Base):

    __tablename__ = 'users'

    user_id = Column(primary_key=True)
    email_address = Column()
    first_name = Column()
    last_name = Column()

    workouts = relationship('Workouts',
                            secondary='users_workouts',
                            back_populates='users')

    def __init__(self, email_address, first_name, last_name):

        """
        Users model.

        Parameters
        ----------
        email_address : String
            Email address.
        first_name : String
            Forename.
        last_name : String
            Surname.
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

