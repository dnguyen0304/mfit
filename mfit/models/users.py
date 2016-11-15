# -*- coding: utf-8 -*-

from sqlalchemy import Column

from mfit import models


class Users(models.Base):

    __tablename__ = 'users'

    id = Column(primary_key=True)
    email_address = Column()
    first_name = Column()
    last_name = Column()

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

        Attributes
        ----------
        id : Integer
            Unique identifier.
        email_address : String
            Email address.
        first_name : String
            Forename.
        last_name : String
            Surname.
        created_at : datetime.datetime
            When the entity was originally created.
        created_by : Integer
            Who originally created the entity.
        updated_at : datetime.datetime
            When the entity was last updated.
        updated_by : Integer
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

